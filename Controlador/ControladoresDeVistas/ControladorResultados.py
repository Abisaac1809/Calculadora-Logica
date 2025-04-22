class ControladorResultados():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, frame_resultados=None, vistas_opciones_resultado=None):
        if not self.__class__._esta_inicializado: 
            if (frame_resultados !=None and vistas_opciones_resultado != None):
                self._frame_opciones_resultado = frame_resultados
                self.vistas_opciones_resultado = vistas_opciones_resultado
                self._nombre_tipo_resultado_seleccionado = "Individual"
                
                self.__class__._esta_inicializado = True
    
    def get_nombre_tipo_resultado_seleccionado(self):
        return self._nombre_tipo_resultado_seleccionado
    
    def get_frame_de(self, nombre_vista:str):
        if (nombre_vista != None and self._frame_opciones_resultado != None):
            vista_principal = self.vistas_opciones_resultado.get(nombre_vista)
            return vista_principal
        else:
            raise ValueError("El nombre de la vista es inválido")
    
    def get_formula_individual(self) -> str:
        frame_resultado_individual = self.get_frame_de("Individual")
        formula = frame_resultado_individual.get_formula()
        
        return formula
    
    def get_lista_formulas_que_se_deben_hacer(self) -> list[str]:
        frame_resultado_completo = self.get_frame_de("Completo")
        lista_formulas = frame_resultado_completo.get_nombre_formulas_que_se_deben_hacer()

        return lista_formulas
    
    def limpiar_entrada_formula(self) -> None:
        frame_resultado_individual = self.get_frame_de("Individual")
        frame_resultado_individual.limpiar_entrada()

    def frame_seleccionado_es(self, nombre_frame: str) -> bool:
        if (nombre_frame != "" and nombre_frame != None):
            if (self._nombre_tipo_resultado_seleccionado == nombre_frame):
                return True
            else:
                return False
        else:
            raise ValueError("El nombre de la vista es inválido")

    def cambiar_frame_a(self, nombre_frame:str) -> None:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.frame_seleccionado_es(nombre_frame)):
                return
            else:
                frame = self.get_frame_de(nombre_frame)
                self._frame_opciones_resultado.cambiar_frame_a(frame)
                self._nombre_tipo_resultado_seleccionado = nombre_frame
        else: 
            raise ValueError("Nombre del frame es inválido")