import customtkinter as ctk
from Controlador.ControladoresDeVistas.ControladorEntradas import *
from Vista.Aplicacion.Componentes.BotonOpcion import *

class MetodosDeEntradaFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)
        self.configure(fg_color="#FAFAFA", corner_radius=0)
        self.controlador_entradas = ControladorEntradas()
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
        
        self.boton_seleccionado = self.boton_manual
        self.boton_seleccionado.configure(fg_color="#C8E6C9", text_color="#2e2e2c")

    def crear_widgets(self):
        self.titulo = ctk.CTkLabel(
            master=self,
            text="Métodos de\nEntrada",
            text_color="#2e2e2c",
            font=("Poppins", 45, "bold")
            )
        
        self.boton_manual = BotonOpcion(self, "Manual")
        self.boton_extraccion = BotonOpcion(self, "Extracción")

    def configurar_widgets(self):
        self.boton_manual.bind("<Button-1>", lambda e: self.seleccionar_frame(self.boton_manual))
        self.boton_extraccion.bind("<Button-1>", lambda e: self.seleccionar_frame(self.boton_extraccion))

    def insertar_widgets(self):
        self.titulo.place(relx=0.0, rely=0.02, relwidth=1, relheight=0.15)
        self.boton_manual.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.1)
        self.boton_extraccion.place(relx=0.0, rely=0.3, relwidth=1, relheight=0.1)

    def seleccionar_frame(self, boton):
        if (boton != None):
            nombre_frame = boton.cget("text")
            if (self.controlador_entradas.frame_seleccionado_es(nombre_frame)):
                return
            else: 
                self.boton_seleccionado.configure(fg_color="transparent", text_color="#424242")
                boton.configure(fg_color="#C8E6C9", text_color="#2e2e2c")
                self.boton_seleccionado = boton
                self.controlador_entradas.cambiar_frame_a(nombre_frame)
        else:
            raise ValueError("Botón no válido")