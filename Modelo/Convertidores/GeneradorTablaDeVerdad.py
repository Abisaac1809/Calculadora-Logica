import itertools
import re
import traceback # Importado para el manejo de errores inesperados

class GeneradorTablaDeVerdad:
    PRECEDENCIA = {
        '¬': 4,
        '∧': 3,
        '∨': 2,
        '→': 1,
        '↔': 1
    }
    ASOCIATIVIDAD_DERECHA = {'→'}

    @classmethod
    def es_operador(cls, token):
        return token in cls.PRECEDENCIA

    @classmethod
    def es_operador_unario(cls, token):
        return token == '¬'

    @classmethod
    def tokenizar(cls, formula):
        if not isinstance(formula, str):
            raise TypeError("La fórmula debe ser una cadena de texto.")
            
        formula_limpia = formula.replace(' ', '')
        if not formula_limpia:
            return [] # Devolver lista vacía para fórmula vacía

        # Patrón para variables de una letra, operadores lógicos y paréntesis
        patron = r'([a-z]|∧|∨|¬|→|↔|\(|\))'
        tokens_encontrados = [match.group(1) for match in re.finditer(patron, formula_limpia)]

        # Validar que todos los caracteres fueron reconocidos por el patrón
        if "".join(tokens_encontrados) != formula_limpia:
            caracteres_invalidos = set(formula_limpia) - set("".join(tokens_encontrados))
            raise ValueError(f"Fórmula contiene caracteres inválidos o no reconocidos: {caracteres_invalidos}")

        return tokens_encontrados

    def shunting_yard(self, tokens):
        salida = []
        pila_operadores = []

        for token in tokens:
            if token.isalpha():
                salida.append(token)
            elif token == '(':
                pila_operadores.append(token)
            elif token == ')':
                while pila_operadores and pila_operadores[-1] != '(':
                    salida.append(pila_operadores.pop())
                if not pila_operadores or pila_operadores[-1] != '(':
                    raise ValueError("Error de sintaxis: Desbalance de paréntesis (posiblemente falta '(').")
                pila_operadores.pop() # Sacar el '('
            elif self.es_operador(token):
                while pila_operadores and pila_operadores[-1] != '(' and self.es_operador(pila_operadores[-1]):
                    op_en_pila = pila_operadores[-1]
                    prec_pila = self.PRECEDENCIA[op_en_pila]
                    prec_token = self.PRECEDENCIA[token]

                    if prec_pila > prec_token or \
                        (prec_pila == prec_token and token not in self.ASOCIATIVIDAD_DERECHA):
                        salida.append(pila_operadores.pop())
                    else:
                        break
                pila_operadores.append(token)
            else:
                # Esto no debería ocurrir si tokenizar funciona bien, pero es una salvaguarda
                raise ValueError(f"Token desconocido encontrado después de tokenizar: '{token}'")


        while pila_operadores:
            operador = pila_operadores.pop()
            if operador == '(':
                raise ValueError("Error de sintaxis: Desbalance de paréntesis (posiblemente sobra '(').")
            salida.append(operador)

        return salida

    def evaluar_postfix(self, expresion_postfix, valores_variables):
        pila_evaluacion = []

        if not expresion_postfix and valores_variables:
            raise ValueError("Expresión postfix vacía no se puede evaluar con variables.")
        if not expresion_postfix and not valores_variables:
            # Podría ser una fórmula vacía originalmente, manejar como inválida o indefinida
            raise ValueError("Expresión postfix vacía.")


        for token in expresion_postfix:
            if token.isalpha():
                if token not in valores_variables:
                    raise ValueError(f"Variable '{token}' no tiene valor asignado en el entorno: {valores_variables}.")
                pila_evaluacion.append(valores_variables[token])
            elif self.es_operador(token):
                try:
                    if self.es_operador_unario(token):
                        operando = pila_evaluacion.pop()
                        pila_evaluacion.append(not operando)
                    else: # Operador binario
                        derecho = pila_evaluacion.pop()
                        izquierdo = pila_evaluacion.pop()
                        if token == '∧':
                            pila_evaluacion.append(izquierdo and derecho)
                        elif token == '∨':
                            pila_evaluacion.append(izquierdo or derecho)
                        elif token == '→':
                            pila_evaluacion.append(not izquierdo or derecho)
                        elif token == '↔':
                            pila_evaluacion.append(izquierdo == derecho)
                except IndexError:
                    raise ValueError(f"Error de sintaxis: Faltan operandos para el operador '{token}'.")
            else:
                # Salvaguarda por si llega un token inesperado
                raise ValueError(f"Token inválido '{token}' durante la evaluación postfix.")


        if len(pila_evaluacion) != 1:
            # Puede ocurrir con expresiones mal formadas como "pq" o "p¬"
            raise ValueError(f"Error de sintaxis: La evaluación finalizó con {len(pila_evaluacion)} valores en la pila en lugar de 1.")
        return pila_evaluacion[0]

    def generar_tabla_verdad(self, formula):
        try:
            tokens = self.tokenizar(formula)
            if not tokens:
                # Manejar fórmula vacía o que solo contenía espacios
                print(f"Advertencia: La fórmula '{formula}' está vacía o no contiene tokens válidos.")
                return [] # Devolver tabla vacía

            if not any(t.isalpha() or self.es_operador(t) for t in tokens):
                raise ValueError(f"La fórmula '{formula}' no contiene variables ni operadores lógicos evaluables.")

            expresion_postfix = self.shunting_yard(tokens)
            variables = sorted(list(set(t for t in tokens if t.isalpha())))

            tabla_resultado = []
            encabezado = variables + [formula] # Usar la fórmula original en el encabezado
            tabla_resultado.append(encabezado)

            if not variables:
                # Caso de fórmula constante (sin variables)
                resultado_constante = self.evaluar_postfix(expresion_postfix, {})
                fila_unica = ['V' if resultado_constante else 'F']
                tabla_resultado.append(fila_unica)
            else:
                # Caso con variables
                num_variables = len(variables)
                for i in range(2**num_variables):
                    valores_bool = [(i >> j) & 1 == 1 for j in range(num_variables - 1, -1, -1)]
                    entorno_actual = dict(zip(variables, valores_bool))
                    resultado_evaluacion = self.evaluar_postfix(expresion_postfix, entorno_actual)

                    fila_valores_str = ['V' if v else 'F' for v in valores_bool]
                    fila_resultado_str = ['V' if resultado_evaluacion else 'F']
                    tabla_resultado.append(fila_valores_str + fila_resultado_str)

            return tabla_resultado

        except (ValueError, TypeError, IndexError) as e:
            print(f"Error al generar la tabla para '{formula}': {e}")
            # Devolver solo encabezado o tabla vacía para indicar el fallo
            return [variables + [formula]] if 'variables' in locals() else [[formula]] if formula else []
        except Exception as e:
            print(f"Error inesperado al procesar '{formula}': {e}")
            traceback.print_exc()
            return [variables + [formula]] if 'variables' in locals() else [[formula]] if formula else []