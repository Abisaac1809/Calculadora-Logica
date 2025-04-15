from Vista.Aplicacion.FrameAplicacion import *
from Vista.Aplicacion.Calculadora.Calculadora import * 
from Vista.Aplicacion.Inicio.Inicio import *

class ControladorFrameAplicacion():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not self.__class__._esta_inicializado: 
            self._frame_aplicacion = None
            self._frame_seleccionado = "Inicio"
            
            self.frames_aplicacion = {
                "Inicio": InicioFrame, 
                "Calculadora Lógica": CalculadoraFrame
                }
            self.__class__._esta_inicializado = True
        
    def set_frame_de_aplicacion(self, frame_aplicacion:ctk.CTkFrame) -> None:
        if (frame_aplicacion != None):
            self._frame_aplicacion = frame_aplicacion
    
    def get_frame_de(self, nombre_frame:str) -> ctk.CTkFrame:
        if (nombre_frame != "" and nombre_frame !=None):
            frame = self.frames_aplicacion.get(nombre_frame)(self._frame_aplicacion)
            return frame
        else:
            raise ValueError("Nombre del frame es inválido")
        
    def cambiar_frame_aplicacion_a(self, nombre_frame:str) -> None:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.is_frame_seleccionado(nombre_frame)):
                return
            else:
                frame = self.get_frame_de(nombre_frame)
                self._frame_aplicacion.cambiar_frame_a(frame)
                self._frame_seleccionado = nombre_frame
        else: 
            raise ValueError("Nombre del frame es inválido")
    
    def is_frame_seleccionado(self, nombre_frame:str) -> bool:
        if (nombre_frame != None):
            if (nombre_frame == self._frame_seleccionado):
                return True
            else: 
                return False
        else:
            raise ValueError("Nombre de frame inválido")