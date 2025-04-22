import customtkinter as ctk
from Vista.Aplicacion.FrameAplicacion import *
from Vista.InicioDeSesion.InicioDeSesion import *
from Vista.Resultado.FrameResultado import *
from Controlador.ControladoresDeVistas.ControladorPrincipal import ControladorVistaPrincipal

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("Vista//Materiales//tema.json")
        self.title("Calculadora Lógica")
        self.iconbitmap("Vista//Materiales//logicIcon.ico")
        self.geometry("1500x700+0+0")
    
        self.vistas_principales = self.get_vistas_principales()
        self.controlador_vista = ControladorVistaPrincipal(self, self.vistas_principales)
        
        self._frame_default = "Inicio Sesion"
        
        self.crear_frame()
        self.insertar_frame()

    def get_vistas_principales(self)->dict[str:ctk.CTkFrame]:
        vista_inicio_sesion = InicioDeSesionFrame 
        vista_aplicacion = FrameAplicacion
        
        vistas_principales = {
            "Inicio Sesion" : vista_inicio_sesion,
            "Aplicacion" : vista_aplicacion,
        }
        
        return vistas_principales

    def crear_frame(self):
        self.frame = self.controlador_vista.get_vista_principal_de(self._frame_default)

    def insertar_frame(self):
        self.frame.pack(expand=True, fill="both")

    def cambiar_frame_a(self, frame:ctk.CTkFrame):
        if (frame != None):
            self.frame.destroy()
            self.frame = frame
            self.frame.pack(expand=True, fill="both")
        else:
            raise ValueError("Frame inválido")
        
    def cambiar_frame_aplicacion(self, frame:ctk.CTkFrame):
        if (frame != None):
            self.frame_aplicacion = self.frame
            self.frame.pack_forget()
            self.frame = frame
            self.frame.pack(expand=True, fill="both")
    
    def volver_frame_aplicacion(self):
        self.frame.pack_forget()
        self.frame.destroy()
        self.frame = self.frame_aplicacion
        self.frame.pack(expand=True, fill="both")