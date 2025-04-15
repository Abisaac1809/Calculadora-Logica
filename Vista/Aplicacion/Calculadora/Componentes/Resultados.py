import customtkinter as ctk
from Controlador.ControladoresDeVistas.ControladorVistaCalculadora import *

class ResultadosFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F1F8E9", corner_radius=0)
        self.tipo_de_resultado = ctk.StringVar(value="Individual")
        self.controlador_vista_calculadora = ControladorVistaCalculadora()

        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
        
    
    def crear_widgets(self):
        self.titulo = ctk.CTkLabel(
            master=self,
            text="Generar\nresultado",
            font=("Poppins", 45, "bold")
            )
        
        self.opcion_individual = ctk.CTkRadioButton(
            master=self,
            text="Individual",
            font=("Poppins", 20),
            variable=self.tipo_de_resultado,
            value="Individual",
            command=self.seleccionar_tipo_resultado
            )
        
        self.opcion_completo = ctk.CTkRadioButton(
            master=self,
            text="Completo",
            font=("Poppins", 20),
            variable=self.tipo_de_resultado,
            value="Completo",
            command=self.seleccionar_tipo_resultado
            )
        
        self.frame_opciones_resultado = FrameResultado(self)
        
        self.mostrar_lenguaje_natural = ctk.CTkCheckBox(
            master=self,
            fg_color="#1B5E20",
            text="Mostrar lenguaje natural",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )
        
        self.mostrar_tabla_verdad = ctk.CTkCheckBox(
            master=self,
            fg_color="#1B5E20",
            text="Mostrar tabla de verdad",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )
        
        self.boton_generar = ctk.CTkButton(
            master=self,
            fg_color="#388E3C",
            text="Generar",
            text_color="#FFFFFF",
            font=("Poppins", 25),
            )
    
    def configurar_widgets(self):
        pass
    
    def insertar_widgets(self):
        self.titulo.pack(fill="both", pady=(20,10))
        self.opcion_individual.pack(fill="both", pady=5, padx=15)
        self.opcion_completo.pack(fill="both", pady=5, padx=15)
        self.frame_opciones_resultado.pack(expand=True, fill="both", pady=10, padx=10)
        self.mostrar_lenguaje_natural.pack(fill="both", pady=5, padx=15)
        self.mostrar_tabla_verdad.pack(fill="both", pady=5, padx=15)
        self.boton_generar.pack(fill="both", pady=20, padx=30, ipady=15)
        
    def seleccionar_tipo_resultado(self) -> None:
        nombre_tipo_resultado = self.tipo_de_resultado.get()
        if (self.controlador_vista_calculadora.es_frame_resultado_seleccionado(nombre_tipo_resultado)):
            return
        else:
            self.controlador_vista_calculadora.cambiar_frame_resultado_a(nombre_tipo_resultado)
            
class FrameResultado(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.controlador = ControladorVistaCalculadora()
        self.controlador.set_frame_opciones_resultado(self)
        self.frame = self.controlador.get_frame_resultado_de("Individual")
        self.frame.pack(expand=True, fill="both")
        
    def cambiar_frame(self, frame:ctk.CTkFrame) -> None:
        if (frame != None):
            self.frame.destroy()
            self.frame = frame
            self.frame.pack(expand=True, fill="both")
        else:
            raise ValueError("Frame inválido")