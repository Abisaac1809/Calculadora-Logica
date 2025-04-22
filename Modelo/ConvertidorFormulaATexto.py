from Modelo.Componentes.ArbolLogico import *

class ConvertidorFormulaATexto:
    def __init__(self):
        self.proposiciones = None
    
    def set_proposiciones(self, proposiciones:dict):
        self.proposiciones = proposiciones
    
    def convertir(self, formula: str) -> str:
        if (self.proposiciones != None and formula != None):
            arbol = ArbolLogico(formula)
            return self._arbol_a_texto(arbol.raiz)
        else:
            raise ValueError("Las proposiciones y la fórmula son inválidas")

    def _arbol_a_texto(self, nodo):
        if nodo is None:
            return ""

        if nodo.valor in self.proposiciones:
            return self.proposiciones[nodo.valor].capitalize()

        if nodo.valor == '¬':
            frase = self._arbol_a_texto(nodo.izquierdo)
            return f"No {frase.lower()}"

        izq = self._arbol_a_texto(nodo.izquierdo)
        der = self._arbol_a_texto(nodo.derecho)

        match nodo.valor:
            case '∧': return f"{izq} y {der.lower()}"
            case '∨': return f"{izq} o {der.lower()}"
            case '→': return f"Si {izq.lower()} entonces {der.lower()}"
            case '↔': return f"{izq} si y solo si {der.lower()}"
            case _: return nodo.valor
