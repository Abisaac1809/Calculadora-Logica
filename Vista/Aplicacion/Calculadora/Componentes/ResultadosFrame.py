import customtkinter as ctk
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrames.ResultadoIndividual import *
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrames.ResultadoCompleto import *
from Controlador.ControladoresDeVistas.ControladorResultados import *

class ResultadosFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F1F8E9", corner_radius=0)
        self.controlador_vistas_resultado = ControladorResultados()
        self.tipo_de_resultado = ctk.StringVar(value="Individual")

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
        if (self.controlador_vistas_resultado.frame_seleccionado_es(nombre_tipo_resultado)):
            return
        else:
            self.controlador_vistas_resultado.cambiar_frame_a(nombre_tipo_resultado)
    
class FrameResultado(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        self.nombre_vista_default = "Individual"
        self.vistas_opciones_resultado = self.get_vistas_opciones_resultado()
        self.controlador_vistas_resultado = ControladorResultados(self, self.vistas_opciones_resultado)

        self.crear_widgets()
        self.insertar_widgets()
    
    def get_vistas_opciones_resultado(self):
        vista_resultado_individual = ResultadoIndividual(self)
        vista_resultado_completo = ResultadoCompleto(self)
        
        frames_opciones_resultado = {
            "Individual" : vista_resultado_individual,
            "Completo" : vista_resultado_completo
            }
        
        return frames_opciones_resultado
    
    def crear_widgets(self):
        self.frame = self.controlador_vistas_resultado.get_frame_de(self.nombre_vista_default)
    
    def insertar_widgets(self):
        self.frame.pack(expand=True, fill="both")
    
    def cambiar_frame_a(self, frame:ctk.CTkFrame) -> None:
        if (frame != None):
            self.frame.pack_forget()
            self.frame = frame
            self.frame.pack(expand=True, fill="both")
        else:
            raise ValueError("Frame inválido")