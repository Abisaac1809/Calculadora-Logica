import customtkinter as ctk
from PIL import Image

class ListaDeProposiciones(ctk.CTkScrollableFrame):
    def __init__(self, master, proposiciones:list=[],**kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F9FAFB", corner_radius=20, border_width=1, border_color="#DADCE0")
        
        longitud_lista_proporcionada = len(proposiciones)
        
        if (longitud_lista_proporcionada > 0):
            self.lista_de_proposiciones = self.generar_proposiciones_por_texto(proposiciones)
        else:
            self.lista_de_proposiciones = []
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.boton_agregar = ctk.CTkButton(
            master=self,
            fg_color="#388E3C",
            text="+ Agregar",
            text_color="#FFFFFF",
            font=("Poppins", 25),
            )
    
    def configurar_widgets(self):
        self.boton_agregar.bind("<Button-1>", lambda evento: self.agregar_proposicion())
    
    def insertar_widgets(self):
        longitud_lista_de_proposiciones = len(self.lista_de_proposiciones)
        
        if (longitud_lista_de_proposiciones > 0):
            for proposicion in self.lista_de_proposiciones:
                proposicion.pack(fill="x", pady=10)
        
        self.boton_agregar.pack(fill="x", pady=10, ipady=8)
    
    def agregar_proposicion(self):
        nueva_proposicion = Proposicion(self)
        
        self.boton_agregar.pack_forget()
        nueva_proposicion.pack(fill="x", pady=10)
        self.boton_agregar.pack(fill="x", pady=10)
        
        self.lista_de_proposiciones.append(nueva_proposicion)
    
    def bloquear_boton_agregar(self):
        self.boton_agregar.destroy()
        
        for frame_proposicion in self.lista_de_proposiciones:
            frame_proposicion.bloquear_boton_borrar()
    
    def generar_proposiciones_por_texto(self, lista_proposiciones_texto:list) -> list:
        lista_proposiciones = []
        
        for nombre,proposicion in lista_proposiciones_texto:
            nueva_proposicion = Proposicion(self)
            nueva_proposicion.fijar_nombre(nombre)
            nueva_proposicion.fijar_proposicion(proposicion)
            
            lista_proposiciones.append(nueva_proposicion)

        return lista_proposiciones


class Proposicion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F1F1F1", border_color="gray", border_width=1, corner_radius=15)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()

    def crear_widgets(self):
        self.cuadrado_entrada_nombre = ctk.CTkFrame(
            master=self,
            fg_color="#C8E6C9",
            border_color="#F1F1F1",
            border_width=2,
            corner_radius=10
            )
        
        self.entrada_nombre = ctk.CTkEntry(
            master=self.cuadrado_entrada_nombre,
            border_color="#C8E6C9",
            fg_color="transparent",
            font=("Poppins", 30, "bold"),
            text_color="#1A1A1A",
            placeholder_text="q",
            placeholder_text_color="#F1F1F1"
            )
            
        self.entrada_proposicion = ctk.CTkEntry(
            master=self,
            border_color="#F1F1F1",
            fg_color="transparent",
            font=("Poppins", 20),
            text_color="#515151",
            placeholder_text="Proposicion"
            )
        
        self.imagen_boton = ctk.CTkImage(
            light_image=Image.open("Vista//Materiales//trash.ico"),
            dark_image=Image.open("Vista//Materiales//trash.ico"),
            size=(32, 32)
            )
        
        self.boton_borrar = ctk.CTkButton(
            master=self,
            text="",
            image=self.imagen_boton,
            )
            
    def configurar_widgets(self):
        self.entrada_nombre.bind("<Return>", lambda evento: self.fijar_nombre(self.entrada_nombre.get()))
        self.entrada_proposicion.bind("<Return>", lambda evento: self.fijar_proposicion(self.entrada_proposicion.get()))

    def insertar_widgets(self):
        self.entrada_nombre.pack(padx=15, pady=5, anchor="center")
        
        self.cuadrado_entrada_nombre.grid(row=0, column=0, sticky="nsew", padx=10, pady=15)
        self.entrada_proposicion.grid(row=0, column=1, columnspan=3, sticky="nsew", padx=10, pady=15)
        self.boton_borrar.grid(row=0, column=4, sticky="nsew", padx=10, pady=15)
        
    def fijar_nombre(self, nombre):
        self.entrada_nombre.destroy()
        
        self.label_nombre = ctk.CTkLabel(
            master=self.cuadrado_entrada_nombre,
            text= nombre,
            font=("Poppins", 30, "bold"),
            text_color="#1A1A1A"
            )
        self.label_nombre.pack(pady=5, anchor="center")
    
    def fijar_proposicion(self, proposicion):
        self.entrada_proposicion.destroy()
        
        self.label_proposicion = ctk.CTkLabel(
            master=self,
            text= proposicion,
            font=("Poppins", 20),
            text_color="#1A1A1A"
        )
        self.label_proposicion.grid(row=0, column=1, columnspan=3, sticky="w", padx=10, pady=15)
        
    def bloquear_boton_borrar(self):
        self.boton_borrar.destroy()