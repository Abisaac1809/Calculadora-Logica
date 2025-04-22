import re
from Modelo.BaseDeDatos.BaseDeDatos import *
from Controlador.ControladoresDeVistas.ControladorPrincipal import *
from Controlador.ControladoresDeUsuario.ControladorDeUsuario import *
from Vista.Admin.FrameAdmin import *
from Modelo.Configuracion.GestionadorDelaConfiguracion import *

class ControladorInicioSesion():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not self.__class__._esta_inicializado:
            self.base_datos = BaseDeDatos("Modelo//BaseDeDatos//Datos.json")
            self.controlador_vista_principal = ControladorVistaPrincipal()
            self.__class__._esta_inicializado = True

    def inicio_sesion(self, nombre:str, contraseña:str, variable:ctk.StringVar):
        if nombre == "Admin" and contraseña == "12345678":
            configurador = ConfigManager()
            frame = ConfigFrame(self.controlador_vista_principal._root_principal, configurador)
            self.controlador_vista_principal._root_principal.cambiar_frame_a(frame)
        else:
            usuario = self.base_datos.iniciar_sesion(nombre, contraseña)
            if usuario:
                ControladorDeUsuario(usuario)
                self.controlador_vista_principal.cambiar_vista_a("Aplicacion")
            else:
                variable.set("Usuario o contraseña inválidos")
        

    def registrar_usuario(self, nombre, contraseña, variable):
        if (not self.validar_usuario(nombre)):
            variable.set("Usuario Inválido: (4-15 caracteres no especiales)") 
        elif (not self.validar_contraseña(contraseña)):
            variable.set("Contraseña inválida: (8-20 caracteres)") 
        else:
            usuario = self.base_datos.registrar_usuario(nombre, contraseña)
            if not usuario:
                variable.set("Usuario ya existe") 
            else:
                ControladorDeUsuario(usuario)
                self.controlador_vista_principal.cambiar_vista_a("Aplicacion")

    def validar_usuario(self, usuario):
        patron = r"^[a-zA-Z0-9_]{4,15}$"
        if re.match(patron, usuario):
            return True
        else:
            return False

    def validar_contraseña(self, contraseña):
        patron = r"^.{8,}$"
        if re.match(patron, contraseña):
            return True
        else:
            return False