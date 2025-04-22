import customtkinter as ctk
from PIL import Image
from Controlador.ControladoresDeUsuario.ControladorDeUsuario import *
from Controlador.ControladoresDeVistas.ControladorEntradas import *

class FrameOtrosProyectos(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#E8F5E9", corner_radius=20, border_width=1, border_color="#DADCE0")
        
        self.controlador_usuario = ControladorDeUsuario()
        self.lista_proyectos_del_usuario = self.controlador_usuario.get_lista_proyectos()
        
        self.crear_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.titulo = ctk.CTkLabel(
            master=self,
            text="Proyectos",
            text_color="#2e2e2c",
            font=("Poppins", 40, "bold")
            )
        
        self.lista_otros_proyectos = ListaOtrosProyectos(self, self.lista_proyectos_del_usuario)
    
    def insertar_widgets(self):
        self.titulo.place(relx=0.0, rely=0.02, relwidth=1, relheight=0.10)
        self.lista_otros_proyectos.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.8)


class ListaOtrosProyectos(ctk.CTkScrollableFrame):
    def __init__(self, master, lista_proyectos_en_texto:list, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F9FAFB", corner_radius=20, border_width=1, border_color="#DADCE0")
        
        frames_de_proyectos = self.generar_lista_frames_de_proyectos(lista_proyectos_en_texto)
        self.insertar_proyectos(frames_de_proyectos)
    
    def insertar_proyectos(self, frames_de_proyectos):
        longitud_lista_frames = len(frames_de_proyectos)
        if (longitud_lista_frames > 0 and frames_de_proyectos != None):
            
            for frame_proyecto in frames_de_proyectos:
                frame_proyecto.pack(fill="x", padx=30, pady=10)
        
        else:
            raise ValueError("La lista de frames de proyectos es inválida")
    
    def generar_lista_frames_de_proyectos(self, lista_proyectos:list)->list:
        longitud_lista_proyectos = len(lista_proyectos)
        
        if (longitud_lista_proyectos > 0):
            frames_de_proyectos = []
            
            for proyecto in lista_proyectos:
                nombre = proyecto.nombre
                numero_proposiciones = proyecto.numero_proposiciones
                nuevo_frame_proyecto = Proyecto(self,proyecto)
                frames_de_proyectos.append(nuevo_frame_proyecto)
                
            return frames_de_proyectos
        else:
            label = ctk.CTkLabel(
                master=self,
                text="Todavía no has realizado ningún proyecto",
                font=("Poppins", 25)
            )
            return [label]


class Proyecto(ctk.CTkFrame):
    def __init__(self, master, proyecto, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F1F1F1", border_color="gray", border_width=1, corner_radius=15)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1), weight=1, uniform="a")

        self.proyecto = proyecto
        self.nombre = proyecto.nombre
        self.numero_proposiciones = proyecto.numero_proposiciones

        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()

    def crear_widgets(self):
        self.nombre_label = ctk.CTkLabel(
            master=self,
            text=self.nombre,
            font=("Poppins", 35)
        )

        self.numero_proposiciones_label = ctk.CTkLabel(
            master=self,
            text=f"{self.numero_proposiciones} Proposiciones",
            font=("Poppins", 20)
        )

        self.imagen_boton = ctk.CTkImage(
            light_image=Image.open("Vista//Materiales//play.ico"),
            dark_image=Image.open("Vista//Materiales//play.ico"),
            size=(32,32)
            )   
        self.boton_continuar = ctk.CTkButton(
            master=self,
            image=self.imagen_boton,
            text="Abrir",
            text_color="#FFFFFF",
            font=("Poppins", 18),
            fg_color="#388E3C",
            hover_color="#1E88E5",
        )

    def configurar_widgets(self):
        self.boton_continuar.bind("<Button-1>", self.continuar)

    def insertar_widgets(self):
        self.nombre_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.numero_proposiciones_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        self.boton_continuar.grid(row=0, column=2, rowspan=2, sticky="e", padx=10, pady=5, ipady=5)

    def continuar(self, evento):
        controlador_entradas = ControladorEntradas()
        proposiciones = self.proyecto.proposiciones
        controlador_entradas.insertar_proposiciones_en_entrada(proposiciones)