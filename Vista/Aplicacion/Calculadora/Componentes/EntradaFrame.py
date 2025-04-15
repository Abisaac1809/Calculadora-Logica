import customtkinter as ctk
from Controlador.ControladoresDeVistas.ControladorEntradas import *
from Vista.Aplicacion.Calculadora.Componentes.Entradas.EntradaManual import *
from Vista.Aplicacion.Calculadora.Componentes.Entradas.EntradaExtraccion import *

class EntradaFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.vistas_de_entrada = self.get_vistas_de_entrada()
        self.controlador_vista_entradas = ControladorEntradas(self, self.vistas_de_entrada)
        self.nombre_frame_default = "Manual"
        
        self.crear_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.frame = self.controlador_vista_entradas.get_frame_de(self.nombre_frame_default)
    
    def insertar_widgets(self):
        self.frame.pack(expand=True, fill="both")
    
    def get_vistas_de_entrada(self):
        vista_entrada_manual = EntradaManual(self)
        vista_entrada_extraccion = EntradaExtraccion(self)
        
        vistas_de_entrada = {
            "Manual" : vista_entrada_manual,
            "Extracción": vista_entrada_extraccion
        }
        
        return vistas_de_entrada

    def cambiar_frame_a(self, frame: ctk.CTkFrame) -> None:
        if (frame != None):
            self.frame.pack_forget()
            self.frame = frame
            self.frame.pack(expand=True, fill="both")
        else:
            raise ValueError("Frame inválido")