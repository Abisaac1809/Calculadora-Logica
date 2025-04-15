import customtkinter as ctk
from Controlador.ControladoresDeVistas.ControladorVistaCalculadora import *
from Vista.Aplicacion.Calculadora.Componentes.MetodosEntrada import *
from Vista.Aplicacion.Calculadora.Componentes.Resultados import *
from Vista.Aplicacion.Calculadora.Componentes.Entradas.EntradaManual import *


class CalculadoraFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color="#BDBDBD")
        
        self.controlador_vistas_calculadora = ControladorVistaCalculadora()
        self.controlador_vistas_calculadora.set_frame_calculadora(self)

        self.entrada_frame_default = "Manual"
        
        self.crear_widgets()
        self.insertar_widgets()
        
    def crear_widgets(self):
        self.metodos_entrada_frame = MetodosDeEntradaFrame(self)
        self.entrada_frame = self.controlador_vistas_calculadora.get_frame_entrada_de(self.entrada_frame_default)
        self.resultados_frame = ResultadosFrame(self)
    
    def insertar_widgets(self):
        self.metodos_entrada_frame.place(relx=0.0, rely=0.001, relwidth=0.2, relheight=1)
        self.entrada_frame.place(relx=0.201, rely=0.001, relwidth=0.499, relheight=1)
        self.resultados_frame.place(relx=0.701, rely=0.001, relwidth=0.3, relheight=1)
    
    def cambiar_frame_metodo_entrada_a(self, frame:ctk.CTkFrame) -> ctk.CTkFrame:
        if (frame != None):
            self.entrada_frame.destroy()
            self.entrada_frame = frame
            self.entrada_frame.place(relx=0.201, rely=0.001, relwidth=0.499, relheight=1)
        else:
            raise ValueError("Frame inválido")
