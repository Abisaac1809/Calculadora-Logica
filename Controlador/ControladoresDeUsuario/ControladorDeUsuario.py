from Modelo.BaseDeDatos.BaseDeDatos import *

class ControladorDeUsuario():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, usuario:Usuario=None):
        if not self.__class__._esta_inicializado:
            self.usuario = usuario
            self.base_de_datos = BaseDeDatos()
            
            self.__class__._esta_inicializado = True
            
    
    def get_nombre_usuario(self):
        return self.usuario.nombre
    
    def get_inicial_nombre_usuario(self):
        nombre = self.usuario.nombre
        inicial = nombre[0].upper()
        return inicial
    
    def get_numero_proyectos(self):
        return self.usuario.numero_proyectos
    
    def get_lista_proyectos(self):
        return self.usuario.proyectos
    
    def get_ultimo_proyecto(self):
        if (self.usuario.numero_proyectos > 0):
            return self.usuario.proyectos[-1]
        else:
            return None
    
    def agregar_nuevo_proyecto(self, nombre:str, proposiciones:dict):
        self.base_de_datos.guardar_proyecto(self.usuario, nombre, proposiciones)
    
    def actualizar_proyectos(self):
        self.usuario = self.base_de_datos.get_usuario(self.usuario.nombre)