import re
from string import ascii_lowercase

class ConvertidorTextoAFormula:
    def __init__(self):
        self.proposiciones = {}
        self.letras = iter(ascii_lowercase)
        self.formula_tokens = []

        self.conectivos = {
            " si y solo si ": "↔",
            " si ": "SI", 
            " entonces ": "→",
            " y ": "∧",
            " o ": "∨"
        }

    def extraer_proposiciones_de(self, texto: str):
        texto = self._limpiar_texto(texto)
        tokens = self._tokenizar(texto)
        self._procesar_tokens(tokens)
        return self.proposiciones

    def get_formula(self) -> str:
        return "".join(self.formula_tokens)

    def _limpiar_texto(self, texto: str) -> str:
        texto = texto.lower()
        texto = re.sub(r'[^\w\sáéíóúñ.,]', '', texto)
        texto = re.sub(r'\s+', ' ', texto)
        texto = texto.replace(",", "")
        texto = texto.replace(".", "")
        return texto.strip()

    def _tokenizar(self, texto: str) -> list:
        for expresion, simbolo in self.conectivos.items():
            texto = texto.replace(expresion, f"|{simbolo}|")
        return [t.strip() for t in texto.split("|") if t.strip()]

    def _asignar_letra(self, frase: str) -> str:
        es_negacion = frase.startswith("no ")
        frase_limpia = frase[3:] if es_negacion else frase
        frase_limpia = frase_limpia.strip().capitalize()

        if frase_limpia not in self.proposiciones.values():
            letra = next(self.letras)
            self.proposiciones[letra] = frase_limpia
        else:
            letra = [k for k, v in self.proposiciones.items() if v == frase_limpia][0]

        return f"¬{letra}" if es_negacion else letra

    def _procesar_tokens(self, tokens: list):
        esperando_entonces = False
        subformula = []

        for token in tokens:
            if token == "SI":
                esperando_entonces = True
                subformula = []
            elif token == "→":
                izquierda = self._agrupar_con_paréntesis(subformula)
                self.formula_tokens.append(izquierda)
                self.formula_tokens.append("→")
                subformula = []
                esperando_entonces = False
            elif token in ["∧", "∨", "↔"]:
                subformula.append(token)
            else:
                letra = self._asignar_letra(token)
                subformula.append(letra)

        if subformula:
            self.formula_tokens.append(self._agrupar_con_paréntesis(subformula))

    def _agrupar_con_paréntesis(self, elementos: list) -> str:
        if len(elementos) == 1:
            return elementos[0]
        resultado = elementos[0]
        i = 1
        while i < len(elementos) - 1:
            operador = elementos[i]
            derecho = elementos[i + 1]
            resultado = f"({resultado}{operador}{derecho})"
            i += 2
        return resultado


