import customtkinter as ctk
from Vista.Aplicacion.Componentes.ListaDeProposiciones import *

class EntradaManual(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="white", corner_radius=0)
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.titulo = ctk.CTkLabel(
            master=self,
            text="Entrada Manual",
            text_color="#2e2e2c",
            font=("Poppins", 45, "bold")
            )
        
        self.texto_label = ctk.CTkLabel(
            master=self,
            text="Proposiciones",
            text_color="#545452",
            font=("Poppins", 30)
            )
        
        self.lista_de_proposiciones = ListaDeProposiciones(self)

    def configurar_widgets(self):
        pass

    def insertar_widgets(self):
        self.titulo.place(relx=0.0, rely=0.02, relwidth=1, relheight=0.15)
        self.texto_label.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.1)
        self.lista_de_proposiciones.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.60)