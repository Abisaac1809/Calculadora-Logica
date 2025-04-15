import customtkinter as ctk
from Vista.Aplicacion.Componentes.ListaDeProposiciones import *

class FrameUltimaEntrada(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#E8F5E9", corner_radius=20, border_width=1, border_color="#DADCE0")
        
        #Se tiene que agregar lógica para sacar lista de la memoria
        self.lista = [("q", "hola"), ("p", "hola otra vez")]
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.titulo = ctk.CTkLabel(
            master=self,
            text="Continua desde donde lo dejaste",
            text_color="#2e2e2c",
            font=("Poppins", 40, "bold")
            )
        
        self.texto_label = ctk.CTkLabel(
            master=self,
            text="Proposiciones utilizadas",
            text_color="#545452",
            font=("Poppins", 30)
            )
        
        self.lista_proposiciones = ListaDeProposiciones(self, self.lista)
        
        self.imagen_boton = ctk.CTkImage(
            light_image=Image.open("Vista//Materiales//play.ico"),
            dark_image=Image.open("Vista//Materiales//play.ico"),
            size=(32,32)
            )   
        self.boton_abrir = ctk.CTkButton(
            master=self,
            image=self.imagen_boton,
            text="Abrir",
            text_color="#FFFFFF",
            font=("Poppins", 18),
            fg_color="#388E3C",
            hover_color="#1E88E5",
        )

    def configurar_widgets(self):
        self.lista_proposiciones.bloquear_boton_agregar()

    def insertar_widgets(self):
        self.titulo.place(relx=0.0, rely=0.02, relwidth=1, relheight=0.10)
        self.texto_label.place(relx=0.1, rely=0.15, relheight=0.1)
        self.lista_proposiciones.place(relx=0.1, rely=0.26, relwidth=0.8, relheight=0.60)
        self.boton_abrir.place(relx=0.35, rely=0.88, relwidth=0.3, relheight=0.1)
        
        