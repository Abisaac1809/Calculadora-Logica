import customtkinter as ctk
from Controlador.ControladoresDeVistas.ControladorEntradas import *
from Vista.Aplicacion.Calculadora.Componentes.MetodosEntrada import *
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrame import *
from Vista.Aplicacion.Calculadora.Componentes.EntradaFrame import *


class CalculadoraFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color="#BDBDBD")
        
        self.crear_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.metodos_entrada_frame = MetodosDeEntradaFrame(self)
        self.entrada_frame = EntradaFrame(self)
        self.resultados_frame = ResultadosFrame(self)
    
    def insertar_widgets(self):
        self.metodos_entrada_frame.place(relx=0.0, rely=0.001, relwidth=0.2, relheight=1)
        self.entrada_frame.place(relx=0.201, rely=0.001, relwidth=0.499, relheight=1)
        self.resultados_frame.place(relx=0.701, rely=0.001, relwidth=0.3, relheight=1)
    
    def agrandar_entrada_frame(self):
        self.resultados_frame.place_forget()
        self.entrada_frame.place(relx=0.201, rely=0.001, relwidth=0.799, relheight=1)
    
    def reducir_entrada_frame(self):
        self.entrada_frame.place(relx=0.201, rely=0.001, relwidth=0.499, relheight=1)
        self.resultados_frame.place(relx=0.701, rely=0.001, relwidth=0.3, relheight=1)
