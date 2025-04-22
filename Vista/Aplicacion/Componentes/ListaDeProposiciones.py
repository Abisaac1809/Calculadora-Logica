import customtkinter as ctk
from PIL import Image
import re
from Controlador.ControladoresDeVistas.ControladorPrincipal import *

class ListaDeProposiciones(ctk.CTkScrollableFrame):
    def __init__(self, master, proposiciones:list=[],**kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F9FAFB", corner_radius=20, border_width=1, border_color="#DADCE0")
        self.controlador_vista_principal = ControladorVistaPrincipal()
        longitud_lista_proporcionada = len(proposiciones)
        
        self.lista_de_proposiciones = []
        if (longitud_lista_proporcionada > 0):
            self.lista_de_proposiciones = self.generar_proposiciones_por_texto(proposiciones)
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def get_lista_proposiciones(self):
        return self.lista_de_proposiciones
    
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
        numero_proposiciones_agregadas = len(self.lista_de_proposiciones)
        if (numero_proposiciones_agregadas > 0):
            ultima_proposicion_agregada = self.lista_de_proposiciones[-1]
            if (not ultima_proposicion_agregada.esta_fijada()):
                self.controlador_vista_principal.mostrar_advertencia("Complete la proposición\npendiente")
                return
            
        nueva_proposicion = Proposicion(self)
        
        self.boton_agregar.pack_forget()
        nueva_proposicion.pack(fill="x", pady=10)
        self.boton_agregar.pack(fill="x", pady=10)
        
        self.lista_de_proposiciones.append(nueva_proposicion)
    
    def borrar_proposicion(self, proposicion_a_borrar):
        if (proposicion_a_borrar != None):
            longitud_lista_de_proposiciones = len(self.lista_de_proposiciones)
            
            for i in range (longitud_lista_de_proposiciones):
                if proposicion_a_borrar == self.lista_de_proposiciones[i]:
                    self.lista_de_proposiciones[i].destroy()
                    self.lista_de_proposiciones.pop(i)
                    return

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
    
    def borrar_toda_las_proposiciones(self):
        while self.lista_de_proposiciones:
            proposicion = self.lista_de_proposiciones.pop()
            proposicion.destroy()
    
    def nombre_existe_en_lista(self, nombre):
        lista = self.lista_de_proposiciones
        for proposicion in lista:
            if proposicion.esta_fijada():
                nombre_proposicion = proposicion.get_nombre()
                if nombre_proposicion == nombre:
                    return True
        return False

class Proposicion(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F1F1F1", border_color="gray", border_width=1, corner_radius=15)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3,4), weight=1, uniform="a")
        self.master = master
        self.controlador_vista_principal = ControladorVistaPrincipal()
        self.nombre_esta_fijado = False
        self.proposicion_esta_fijada = False
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
        self.entrada_nombre.focus()

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
        self.entrada_nombre.bind("<KeyRelease>", self.validar_entrada_nombre)
        self.entrada_proposicion.bind("<KeyRelease>", self.validar_entrada_proposicion)
        self.boton_borrar.bind("<Button-1>", self.borrar)

    def insertar_widgets(self):
        self.entrada_nombre.pack(padx=15, pady=5, anchor="center")
        
        self.cuadrado_entrada_nombre.grid(row=0, column=0, sticky="nsew", padx=10, pady=15)
        self.entrada_proposicion.grid(row=0, column=1, columnspan=3, sticky="nsew", padx=10, pady=15)
        self.boton_borrar.grid(row=0, column=4, sticky="nsew", padx=10, pady=15)

    def fijar_nombre(self, nombre):
        if self.master.nombre_existe_en_lista(nombre):
            self.controlador_vista_principal.mostrar_advertencia("El nombre ya\nestá en uso")
            return
        else:
            self.entrada_nombre.destroy()
            
            self.label_nombre = ctk.CTkLabel(
                master=self.cuadrado_entrada_nombre,
                text= nombre,
                font=("Poppins", 30, "bold"),
                text_color="#1A1A1A"
                )
            self.label_nombre.pack(pady=5, anchor="center")
            self.entrada_proposicion.focus()
            self.nombre_esta_fijado = True

    def fijar_proposicion(self, proposicion):
        self.entrada_proposicion.destroy()
        
        self.label_proposicion = ctk.CTkLabel(
            master=self,
            text= proposicion,
            font=("Poppins", 20),
            text_color="#1A1A1A"
        )
        self.label_proposicion.grid(row=0, column=1, columnspan=3, sticky="w", padx=10, pady=15)
        
        self.proposicion_esta_fijada = True
    
    def esta_fijada(self)->bool:
        if (self.nombre_esta_fijado and self.proposicion_esta_fijada):
            return True
        else:
            return False
    
    def get_nombre(self) -> str:
        if self.nombre_esta_fijado:
            return self.label_nombre.cget("text")
    
    def get_proposicion(self) -> str:
        if self.proposicion_esta_fijada:
            return self.label_proposicion.cget("text")
    
    def borrar(self, evento):
        self.master.borrar_proposicion(self)

    def bloquear_boton_borrar(self):
        self.boton_borrar.destroy()

    def validar_entrada_nombre(self, evento):
        texto_actual = self.entrada_nombre.get()
        
        if evento.keysym == "BackSpace":
            return
        
        if len(texto_actual) > 1:
            self.entrada_nombre.delete(1, "end")
            self.controlador_vista_principal.mostrar_advertencia("Máximo una letra")
            
        if (texto_actual.isalpha()):
            if (texto_actual.isupper()):
                texto_actual = texto_actual.lower()
                self.entrada_nombre.delete(0, "end")
                self.entrada_nombre.insert(0, texto_actual)
            else:
                return
        
        else:
            self.entrada_nombre.delete(0, "end")
            self.controlador_vista_principal.mostrar_advertencia("Solo se permite letras")

    def patrón_es_valido(self, texto_nuevo: str)->bool:
        patron_permitido = r'^[a-zA-Z0-9\- ]*$'  
        return re.fullmatch(patron_permitido, texto_nuevo) is not None

    def validar_entrada_proposicion(self, event)->None:
        texto_actual = self.entrada_proposicion.get()
        if not self.patrón_es_valido(texto_actual):
            texto_filtrado = re.sub(r'[^a-zA-Z0-9\- ]', '', texto_actual)
            self.entrada_proposicion.delete(0, ctk.END)
            self.entrada_proposicion.insert(0, texto_filtrado)
            self.controlador_vista_principal.mostrar_advertencia("No se permiten\n caracteres especiales")