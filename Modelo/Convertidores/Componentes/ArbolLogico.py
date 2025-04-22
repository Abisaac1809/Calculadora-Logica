from Modelo.Convertidores.Componentes.Nodo import *
class ArbolLogico:
    def __init__(self, formula: str):
        self.tokens = self.tokenizar(formula)
        self.pos = 0
        self.raiz = self.parse_implicacion()

    def tokenizar(self, formula):
        formula = formula.replace('(', ' ( ').replace(')', ' ) ')
        for s in ['¬', '∧', '∨', '→', '↔']:
            formula = formula.replace(s, f' {s} ')
        return formula.split()

    def parse_implicacion(self):
        nodo = self.parse_bicondicional()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '→':
            op = self.tokens[self.pos]
            self.pos += 1
            nodo = Nodo(op, nodo, self.parse_bicondicional())
        return nodo

    def parse_bicondicional(self):
        nodo = self.parse_disyuncion()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '↔':
            op = self.tokens[self.pos]
            self.pos += 1
            nodo = Nodo(op, nodo, self.parse_disyuncion())
        return nodo

    def parse_disyuncion(self):
        nodo = self.parse_conjuncion()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '∨':
            op = self.tokens[self.pos]
            self.pos += 1
            nodo = Nodo(op, nodo, self.parse_conjuncion())
        return nodo

    def parse_conjuncion(self):
        nodo = self.parse_negacion()
        while self.pos < len(self.tokens) and self.tokens[self.pos] == '∧':
            op = self.tokens[self.pos]
            self.pos += 1
            nodo = Nodo(op, nodo, self.parse_negacion())
        return nodo

    def parse_negacion(self):
        if self.tokens[self.pos] == '¬':
            self.pos += 1
            return Nodo('¬', self.parse_negacion())
        elif self.tokens[self.pos] == '(':
            self.pos += 1
            nodo = self.parse_implicacion()
            self.pos += 1  # salta ')'
            return nodo
        else:
            simbolo = self.tokens[self.pos]
            self.pos += 1
            return Nodo(simbolo)