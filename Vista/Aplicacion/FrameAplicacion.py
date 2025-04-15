import customtkinter as ctk
from Vista.Aplicacion.Componentes.BarraMenu import BarraMenu
from Controlador.ControladoresDeVistas.ControladorFramesAplicacion import ControladorFrameAplicacion

class FrameAplicacion(ctk.CTkFrame):
    def __init__(self, master:ctk.CTk):
        super().__init__(master=master)
        self.controlador_frames_aplicacion = ControladorFrameAplicacion()
        self.controlador_frames_aplicacion.set_frame_de_aplicacion(self)
        self.frame_default = "Inicio"
        
        self.crear_widgets()
        self.insertar_widgets()
    
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
            self.frame.pack_forget()
            self.frame = frame
            self.frame.place(relx=0.0, rely=0.1, relwidth=1, relheight=0.9)
        else:
            raise ValueError("Frame inválido")