import customtkinter as ctk
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrames.Teclado import *

class ResultadoIndividual(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
        
    def crear_widgets(self):
        self.operacion_entry = ctk.CTkEntry(
            self,
            fg_color="#FFFFFF",
            border_color="#C8E6C9",
            font=("Poppins", 25),
            corner_radius=10,
            placeholder_text="Fórmula"
            )
        
        self.teclado = Teclado(self, self.operacion_entry)
    
    def configurar_widgets(self):
        pass

    def insertar_widgets(self):
        self.operacion_entry.pack(fill="both", pady=10, padx=20, ipady=20)
        self.teclado.pack(expand=True, fill="both", pady=10, padx=20)