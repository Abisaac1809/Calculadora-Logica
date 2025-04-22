import customtkinter as ctk
import re
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrames.Teclado import *
from Controlador.ControladoresDeVistas.ControladorPrincipal import *

class ResultadoIndividual(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.controlador_vista_principal = ControladorVistaPrincipal()
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
        
    def crear_widgets(self):
        self.entrada_operacion = ctk.CTkEntry(
            self,
            fg_color="#FFFFFF",
            border_color="#C8E6C9",
            font=("Poppins", 25),
            corner_radius=10,
            placeholder_text="Fórmula"
            )
        
        self.teclado = Teclado(self, self.entrada_operacion)
    
    def configurar_widgets(self):
        self.entrada_operacion.bind("<KeyRelease>", self.validar_entrada_formula)

    def insertar_widgets(self):
        self.entrada_operacion.pack(fill="both", pady=10, padx=20, ipady=20)
        self.teclado.pack(expand=True, fill="both", pady=10, padx=20)
    
    def get_formula(self):
        formula = self.entrada_operacion.get()

        return formula

    def limpiar_entrada(self):
        self.entrada_operacion.delete(0, ctk.END)

    def patron_es_valido(self, texto_nuevo: str)->bool:
        patron_permitido = r'^[a-z¬∧∨→↔]*$'  
        return re.fullmatch(patron_permitido, texto_nuevo) is not None

    def validar_entrada_formula(self, event)->None:
        texto_actual = self.entrada_operacion.get()
        if not self.patron_es_valido(texto_actual):
            texto_filtrado = re.sub(r'[^a-z¬∧∨→↔]*$', '', texto_actual)
            self.entrada_operacion.delete(0, ctk.END)
            self.entrada_operacion.insert(0, texto_filtrado)
            self.controlador_vista_principal.mostrar_advertencia("No se permiten\n caracteres especiales")