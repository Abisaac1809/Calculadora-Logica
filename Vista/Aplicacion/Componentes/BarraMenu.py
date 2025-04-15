import customtkinter as ctk
from Vista.Aplicacion.Componentes.BotonOpcion import BotonOpcion
from Controlador.ControladoresDeVistas.ControladorFramesAplicacion import *
import datetime

class BarraMenu(ctk.CTkFrame):
    def __init__(self, master:ctk.CTkFrame):
        super().__init__(master=master)
        self.configure(fg_color="#F5F7FA")
        
        self.controlador_frame_aplicacion = ControladorFrameAplicacion()
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
        
        boton_default = self.boton_inicio
        self.boton_seleccionado = boton_default
        self.boton_seleccionado.configure(fg_color="#C8E6C9", text_color="#2e2e2c")
        
    def crear_widgets(self):
        self.cuadrado_fecha = CuadradoConContenido(self, "14") # insertar fecha
        self.cuadrado_perfil = CuadradoConContenido(self, "A") # insertar lógica de usuario
        
        self.frame_opciones_de_ventana = ctk.CTkFrame(self, fg_color="transparent")
        self.boton_inicio = BotonOpcion(self.frame_opciones_de_ventana, "Inicio")
        self.boton_calculadora_logica = BotonOpcion(self.frame_opciones_de_ventana, "Calculadora Lógica")
        
    def configurar_widgets(self):
        self.boton_inicio.bind("<Button-1>", lambda e: self.seleccionar_frame(self.boton_inicio))
        self.boton_calculadora_logica.bind("<Button-1>", lambda e: self.seleccionar_frame(self.boton_calculadora_logica))
    
    def insertar_widgets(self):
        self.cuadrado_fecha.place(relx=0.01, rely=0.2, relwidth=0.04, relheight=0.6)
        self.cuadrado_perfil.place(relx=0.95, rely=0.2, relwidth=0.04, relheight=0.6)
        
        self.frame_opciones_de_ventana.place(relx=0.1, rely=0.0, relwidth=0.8, relheight=1)
        self.boton_inicio.pack(fill="y", side="left", ipadx=10)
        self.boton_calculadora_logica.pack(fill="y", side="left", ipadx=10)
    
    def seleccionar_frame(self, boton):
        if (boton != None):
            nombre_frame = boton.cget("text")
            if (self.controlador_frame_aplicacion.is_frame_seleccionado(nombre_frame)):
                return
            else: 
                self.boton_seleccionado.configure(fg_color="transparent", text_color="#424242")
                boton.configure(fg_color="#C8E6C9", text_color="#2e2e2c")
                self.boton_seleccionado = boton
                self.controlador_frame_aplicacion.cambiar_frame_aplicacion_a(nombre_frame)
        else:
            raise ValueError("Botón no válido")
            

class CuadradoConContenido(ctk.CTkFrame):
    def __init__(self, master:ctk.CTkFrame, texto:str):
        super().__init__(master=master)
        self.configure(
            fg_color="white",
            border_color="#9bbd7f",
            border_width=2,
            corner_radius=10
            )
        
        self.label = ctk.CTkLabel(
            master=self,
            text= texto,
            font=("Poppins", 25, "bold"),
            text_color="#515151"
            )
        self.label.pack(padx=5, pady=5)