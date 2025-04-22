from Controlador.ControladoresDeVistas.ControladorPrincipal import *
from Controlador.ControladoresDeVistas.ControladorEntradas import *
from Controlador.ControladoresDeVistas.ControladorResultados import *
from Modelo.ConvertidorFormulaATexto import * 
from Modelo.GeneradorTablaDeVerdad import * 
from Modelo.ConvertidorTextoAFormula import *

class ControladorDeOperaciones():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not self.__class__._esta_inicializado:
            self.extractor_de_proposiciones = ExtractorDeProposiciones()
            self.extractor_de_formulas = ExtractorDeFormulas()
            self.convertidor_formula_a_texto = ConvertidorFormulaATexto()
            self.generador_tabla_de_verdad = GeneradorTablaDeVerdad()
            self.convertidor_texto_a_formula = ConvertidorTextoAFormula()
            
            
            self.__class__._esta_inicializado = True
    
    def mostrar_resultado_manual(self):
            controlador_vista_principal = ControladorVistaPrincipal()
            resultados = self.generar_resultados_manual()
            if resultados == None:
                return
            controlador_vista_principal.mostrar_resultado(resultados)
        
    def mostrar_resultado_extraccion(self, texto:str):
        controlador_vista_principal = ControladorVistaPrincipal()
        resultados = self.generar_resultado_extraccion(texto)
        
        controlador_vista_principal.mostrar_resultado(resultados)
    
    def generar_resultados_manual(self) -> list[dict]:
        try:
            proposiciones = self.extractor_de_proposiciones.extraer_proposiciones()
            formulas = self.extractor_de_formulas.extraer_formulas_manual(proposiciones)
            textos_convertidos = self.generar_texto_convertido(proposiciones, formulas)
            tablas_de_verdad = self.generar_tablas_de_verdad(formulas)
        except Exception as e:
            return None
        
        resultados = []
        cantidad_de_formulas = len(formulas)
        
        for i in range(cantidad_de_formulas):
            nuevo_resultado = {
                "Proposiciones": proposiciones,
                "Formula" : formulas[i],
                "Texto" : textos_convertidos[i],
                "Tabla" : tablas_de_verdad[i]
            }
            resultados.append(nuevo_resultado)
        
        return resultados
    
    def generar_resultado_extraccion(self, texto:str):
        proposiciones = self.convertidor_texto_a_formula.extraer_proposiciones_de(texto)
        formulas = [self.convertidor_texto_a_formula.get_formula()]
        textos_convertidos = self.generar_texto_convertido(proposiciones, formulas)
        tablas_de_verdad = self.generar_tablas_de_verdad(formulas)
        
        resultados = []
        cantidad_de_formulas = len(formulas)
        
        for i in range(cantidad_de_formulas):
            nuevo_resultado = {
                "Proposiciones": proposiciones,
                "Formula" : formulas[i],
                "Texto" : textos_convertidos[i],
                "Tabla" : tablas_de_verdad[i]
            }
            resultados.append(nuevo_resultado)
        
        return resultados
    
    def generar_texto_convertido(self, proposiciones:dict, formulas:list):
        if (proposiciones != None and formulas != None):
            textos_convertidos = []
            self.convertidor_formula_a_texto.set_proposiciones(proposiciones)
            for formula in formulas:
                nuevo_texto_convertido = self.convertidor_formula_a_texto.convertir(formula)
                textos_convertidos.append(nuevo_texto_convertido)
            return textos_convertidos
        else:
            raise ValueError("Las proposiciones y fórmulas son inválidas")
    
    def generar_tablas_de_verdad(self, formulas:list) -> list:
        if (formulas != None):
            tablas_de_verdad = []
            for formula in formulas:
                nueva_tabla_de_verdad = self.generador_tabla_de_verdad.generar_tabla_verdad(formula)
                tablas_de_verdad.append(nueva_tabla_de_verdad)
            return tablas_de_verdad
        else:
            raise ValueError("Las fórmulas son inválidas")


class ExtractorDeProposiciones():
    def __init__(self):
        self.controlador_tipo_entrada = ControladorEntradas()
        
        self.tipos_de_extraccion = {
            "Manual": self.extraer_proposiciones_manuales,
            "Extraccion": self.extraer_proposiciones_de_texto
        }

    def extraer_proposiciones(self) -> list:
        nombre_tipo_extraccion = self.controlador_tipo_entrada.get_nombre_tipo_entrada_seleccionada()
        proposiciones = self.tipos_de_extraccion.get(nombre_tipo_extraccion)()
        
        return proposiciones

    def extraer_proposiciones_manuales(self) -> list:
        proposiciones = self.controlador_tipo_entrada.get_diccionario_proposiciones_manuales()
        if len(proposiciones) < 4:
            controlador_vista_principal = ControladorVistaPrincipal()
            controlador_vista_principal.mostrar_advertencia("Debes ingresar al menos\n 4 proposiciones")
            return None
        self.controlador_tipo_entrada.borrar_todas_las_proposiciones_manuales()
        
        return proposiciones

    def extraer_proposiciones_de_texto(self, texto:str) -> dict[str:str]:
        proposiciones = self.convertidor_texto_a_proposiciones.extraer_proposiciones_de(texto)
        
        return proposiciones


class ExtractorDeFormulas():
    def __init__(self):
        self.controlador_de_tipo_resultado = ControladorResultados()
        
        self.tipos_de_extraccion = {
            "Individual" : self.extraer_formula_resultado_individual,
            "Completo" : self.extraer_formulas_resultado_completo
        }
    
    def extraer_formulas_manual(self, proposiciones:dict) -> list:
        nombre_tipo_extraccion = self.controlador_de_tipo_resultado.get_nombre_tipo_resultado_seleccionado()
        formulas = self.tipos_de_extraccion.get(nombre_tipo_extraccion)(proposiciones)

        return formulas

    def extraer_formula_resultado_individual(self, proposiciones:dict) -> list:
        formula = self.controlador_de_tipo_resultado.get_formula_individual()
        
        if (self.es_formula_logica_valida(formula)):
            for caracter in formula:
                if caracter.isalpha():
                    if (proposiciones.get(caracter, None)):
                        self.controlador_de_tipo_resultado.limpiar_entrada_formula()
                    else:
                        controlador_vista_principal = ControladorVistaPrincipal()
                        controlador_vista_principal.mostrar_advertencia("Ingresa proposiciones válidas")
                        return None
            return [formula]
        else: 
            controlador_vista_principal = ControladorVistaPrincipal()
            controlador_vista_principal.mostrar_advertencia("La fórmula que has\ningresado es inválida")

    def extraer_formulas_resultado_completo(self, proposiciones:dict) -> list:
        self.conectivos = {
            "Negacion" : "¬",
            "Conjuncion" : "∧", 
            "Disyuncion": "∨",
            "Condicional": "→",
            "Bicondicional": "↔",
        }
        lista_formulas_por_hacer = self.controlador_de_tipo_resultado.get_lista_formulas_que_se_deben_hacer()
        formulas = []
        
        for nombre_formula in lista_formulas_por_hacer:
            formula = ""
            conectivo = self.conectivos.get(nombre_formula)
            numero_proposiciones = len(proposiciones)
            nombres_de_proposiciones = list(proposiciones.keys())
            
            for i in range(numero_proposiciones):
                nombre_de_proposicion = nombres_de_proposiciones[i]
                if (i == numero_proposiciones-1):
                    formula += f"{nombre_de_proposicion}"
                else:
                    formula+= f"{nombre_de_proposicion}{conectivo}"
            
            formulas.append(formula)
        return formulas
    
    def extraer_formula_texto(self):
        self.convertidor_texto_a_proposiciones.get_formula()
        
    def es_formula_logica_valida(self, formula: str) -> bool:
        OPERADORES_BINARIOS = {'∧', '∨', '→', '↔'}
        OPERADOR_NEGACION = '¬'
        PARENTESIS_ABIERTO = '('
        PARENTESIS_CERRADO = ')'
        PROPOSICIONES_VALIDAS = set('abcdefghijklmnopqrstuvwxyz')
        
        ESPERANDO_OPERANDO = True
        ESPERANDO_OPERADOR = False
        
        pila_parentesis = []
        estado_actual = ESPERANDO_OPERANDO
        
        for posicion, caracter in enumerate(formula):
            if caracter not in PROPOSICIONES_VALIDAS and \
            caracter not in OPERADORES_BINARIOS and \
            caracter != OPERADOR_NEGACION and \
            caracter not in {PARENTESIS_ABIERTO, PARENTESIS_CERRADO}:
                return False
            
            if caracter in PROPOSICIONES_VALIDAS:
                if not estado_actual == ESPERANDO_OPERANDO:
                    return False
                estado_actual = ESPERANDO_OPERADOR
            
            elif caracter == OPERADOR_NEGACION:
                if not estado_actual == ESPERANDO_OPERANDO:
                    return False
                if posicion + 1 >= len(formula):
                    return False
            
            elif caracter in OPERADORES_BINARIOS:
                if estado_actual == ESPERANDO_OPERANDO:
                    return False
                estado_actual = ESPERANDO_OPERANDO
            
            elif caracter == PARENTESIS_ABIERTO:
                if not estado_actual == ESPERANDO_OPERANDO and \
                (posicion > 0 and formula[posicion-1] not in OPERADORES_BINARIOS | {OPERADOR_NEGACION, PARENTESIS_ABIERTO}):
                    return False
                pila_parentesis.append(caracter)
                estado_actual = ESPERANDO_OPERANDO
            
            elif caracter == PARENTESIS_CERRADO:
                if estado_actual == ESPERANDO_OPERANDO and \
                (posicion == 0 or formula[posicion-1] in OPERADORES_BINARIOS | {OPERADOR_NEGACION, PARENTESIS_ABIERTO}):
                    return False
                if not pila_parentesis or pila_parentesis.pop() != PARENTESIS_ABIERTO:
                    return False
                estado_actual = ESPERANDO_OPERADOR
        
        return not pila_parentesis and not estado_actual == ESPERANDO_OPERANDO