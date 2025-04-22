import customtkinter as ctk
from Controlador.ControladoresDeInicioSesion.ControladorInicioSesion import *

class Menu(ctk.CTkFrame):
    def __init__(self, padre):
        super().__init__(master=padre, fg_color="transparent")
        self.controlador = ControladorInicioSesion()
        self.switch_var = ctk.StringVar(value="dark")
        self.usuario_existe_var = ctk.StringVar(value="")
        
        self.crear_widgets()
        self.configurar_widgets()
        self.pack_widgets()
        
    def crear_widgets(self):

        self.titulo = ctk.CTkLabel(
            self,
            text="¡Bienvenido!",
            font=("Poppins", 70)
            )
        
        self.usuario_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ingresa tu Usuario",
            font=("Poppins", 30),
            corner_radius=20
            )
        
        self.contraseña_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ingresa tu Contraseña",
            font=("Poppins", 30),
            corner_radius=20
            )
        
        self.usuario_existe_label = ctk.CTkLabel(
            self,
            textvariable=self.usuario_existe_var,
            font=("Poppins", 18),
            text_color="red", 
            )
        
        self.inicio_boton = ctk.CTkButton(
            self,
            text="Iniciar Sesión",
            font=("Poppins", 30),
            corner_radius=20
            )
        
        self.cuenta_label = ctk.CTkLabel(
            self,
            text="¿No tienes cuenta?",
            font=("Poppins", 18),
            justify="left"
            )
        
        self.crear_boton = ctk.CTkButton(
            self,
            text="Crear Cuenta",
            font=("Poppins", 30),
            corner_radius=20
            )

    def configurar_widgets(self):

        self.usuario_entry.bind("<Return>", lambda evento: self.contraseña_entry.focus())
        self.contraseña_entry.bind("<Return>", lambda evento: self.iniciar_sesion(evento))
        self.inicio_boton.bind("<Button-1>", self.iniciar_sesion)
        self.crear_boton.bind("<Button-1>", self.crear_cuenta)

    def pack_widgets(self):
        self.titulo.pack(expand=True, fill="both", pady=10, padx=40)
        self.usuario_entry.pack(expand=True, fill="both", padx=40, pady=10)
        self.contraseña_entry.pack(expand=True, fill="both", padx=40, pady=10)
        self.usuario_existe_label.pack(fill="x")
        self.inicio_boton.pack(expand=True, fill="both", padx=60, pady=(5, 30))
        self.cuenta_label.pack(fill="x", padx=60)
        self.crear_boton.pack(expand=True, fill="both", padx=60, pady=(0, 30))

    def iniciar_sesion(self, evento):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()
        if (usuario != "" and contraseña != ""):
            self.controlador.inicio_sesion(usuario, contraseña, self.usuario_existe_var)
        else:
            self.usuario_existe_var.set("Llene todos los campos")

    def crear_cuenta(self, evento):
        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()
        if (usuario != "" and contraseña != ""):
            self.controlador.registrar_usuario(usuario, contraseña, self.usuario_existe_var)
        else:
            self.usuario_existe_var.set("Llene todos los campos")