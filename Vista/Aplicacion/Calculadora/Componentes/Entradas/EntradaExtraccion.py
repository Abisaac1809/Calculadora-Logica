import customtkinter as ctk
from Controlador.ControladoresDeVistas.ControladorPrincipal import *
from Controlador.ControladoresDeOperaciones.ControladorOperaciones import *

class EntradaExtraccion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#FFFFFF", corner_radius=0)
        self.controlador_vista_principal = ControladorVistaPrincipal()
        self.controlador_de_resultados = ControladorDeOperaciones()

        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.titulo = ctk.CTkLabel(
            master=self,
            text="Extracción de texto",
            text_color="#2e2e2c",
            font=("Poppins", 45, "bold")
            )
        
        self.texto_label = ctk.CTkLabel(
            master=self,
            text="Texto",
            text_color="#545452",
            font=("Poppins", 30)
            )

        self.caja_texto = ctk.CTkTextbox(
            master=self,
            border_color="#C8E6C9",
            border_width=1,
            text_color="#0D47A1",
            font=("Poppins", 20)
            )
        
        self.frame_de_botones = ctk.CTkFrame(self, fg_color="transparent")
        
        self.borrar_boton = ctk.CTkButton(
            master=self.frame_de_botones,
            fg_color="#388E3C",
            text_color="#FFFFFF",
            text="Borrar",
            font=("Poppins", 25),
            )
        
        self.extraer_boton = ctk.CTkButton(
            master=self.frame_de_botones,
            fg_color="#388E3C",
            text_color="#FFFFFF",
            text="Extraer",
            font=("Poppins", 25)
            )
    
    def configurar_widgets(self):
        self.borrar_boton.bind("<Button-1>", self.borrar_texto)
        self.extraer_boton.bind("<Button-1>", self.generar_resultados)
        self.caja_texto.bind("<Return>", self.generar_resultados)

    def insertar_widgets(self):
        self.borrar_boton.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        self.extraer_boton.pack(side="left", expand=True, fill="both", padx=10, pady=10)
        
        self.titulo.place(relx=0.0, rely=0.02, relwidth=1, relheight=0.15)
        self.texto_label.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
        self.caja_texto.place(relx=0.1, rely=0.31, relwidth=0.8, relheight=0.30)
        self.frame_de_botones.place(relx=0.1, rely=0.63, relwidth=0.8, relheight=0.1)
    
    def generar_resultados(self, evento):
        texto = self.caja_texto.get("0.0", ctk.END)
        self.caja_texto.delete("0.0", ctk.END)
        if (texto != ""):
            self.controlador_de_resultados.mostrar_resultado_extraccion(texto)
        else:
            self.controlador_vista_principal.mostrar_advertencia("Texto ingresado es inválido")
    
    def borrar_texto(self, evento):
        self.caja_texto.delete("0.0", ctk.END)
    