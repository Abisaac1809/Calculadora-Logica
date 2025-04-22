import customtkinter as ctk
from Vista.Aplicacion.Inicio.Componentes.FrameTexto import *
from Vista.Aplicacion.Inicio.Componentes.FrameUltimaEntrada import *
from Vista.Aplicacion.Inicio.Componentes.FrameOtrosProyectos import *
from Controlador.ControladoresDeUsuario.ControladorDeUsuario import *

class InicioFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F5F7FA")

        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.frame_texto = FrameTexto(self)
        self.frame_ultima_entrada = FrameUltimaEntrada(self)
        self.frame_otros_proyectos = FrameOtrosProyectos(self)

    def configurar_widgets(self):
        pass

    def insertar_widgets(self):
        self.frame_texto.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.2)
        self.frame_ultima_entrada.place(relx=0.02, rely=0.24, relwidth=0.48, relheight=0.74)
        self.frame_otros_proyectos.place(relx=0.52, rely=0.24, relwidth=0.46, relheight=0.74)
    
    def actualizar_proyectos_inicio(self):
        controlador_usuario = ControladorDeUsuario()
        controlador_usuario.actualizar_proyectos()
        
        self.frame_ultima_entrada.destroy()
        self.frame_otros_proyectos.destroy()

        self.frame_ultima_entrada = FrameUltimaEntrada(self)
        self.frame_otros_proyectos = FrameOtrosProyectos(self)

        self.frame_ultima_entrada.place(relx=0.02, rely=0.24, relwidth=0.48, relheight=0.74)
        self.frame_otros_proyectos.place(relx=0.52, rely=0.24, relwidth=0.46, relheight=0.74)