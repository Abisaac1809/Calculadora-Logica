import customtkinter as ctk
from Vista.Aplicacion.Componentes.BarraMenu import BarraMenu
from Vista.Aplicacion.Inicio.Inicio import *
from Vista.Aplicacion.Calculadora.Calculadora import *
from Controlador.ControladoresDeVistas.ControladorAplicacion import ControladorFrameAplicacion

class FrameAplicacion(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.frame_default = "Inicio"
        
        self.vistas_aplicacion = self.get_vistas_aplicacion()
        self.controlador_frames_aplicacion = ControladorFrameAplicacion(self, self.vistas_aplicacion)
        
        self.crear_widgets()
        self.insertar_widgets()
    
    def get_vistas_aplicacion(self)->dict[str:ctk.CTkFrame]:
        vista_inicio = InicioFrame(self)
        vista_calculadora = CalculadoraFrame(self)
        
        vistas_aplicacion = {
            "Inicio" : vista_inicio,
            "Calculadora Lógica": vista_calculadora
        }
        
        return vistas_aplicacion

    def crear_widgets(self):
        self.barra_menu = BarraMenu(self)
        self.separacion = ctk.CTkFrame(self, fg_color="#DADCE0")
        self.frame = self.controlador_frames_aplicacion.get_frame_de(self.frame_default)

    def insertar_widgets(self):
        self.barra_menu.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.1)
        self.separacion.place(relx=0.0, rely=0.0991, relwidth=1, relheight= 0.009)
        self.frame.place(relx=0.0, rely=0.1, relwidth=1, relheight=0.9)

    def cambiar_frame_a(self, frame: ctk.CTkFrame) -> None:
        if (frame != None):
            self.frame.place_forget()
            self.frame = frame
            self.frame.place(relx=0.0, rely=0.1, relwidth=1, relheight=0.9)
        else:
            raise ValueError("Frame inválido")