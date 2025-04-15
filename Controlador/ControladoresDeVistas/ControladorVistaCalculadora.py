from Vista.Aplicacion.FrameAplicacion import *
from Vista.Aplicacion.Calculadora.Componentes.Entradas.EntradaManual import *
from Vista.Aplicacion.Calculadora.Componentes.Entradas.EntradaExtraccion import *
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrames.ResultadoIndividual import *
from Vista.Aplicacion.Calculadora.Componentes.ResultadosFrames.ResultadoCompleto import *

class ControladorVistaCalculadora():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not self.__class__._esta_inicializado: 
            self._frame_calculadora = None
            self._frame_opciones_resultado = None
            
            self._frame_entrada_seleccionado = "Manual"
            self._frame_resultado_seleccionado = "Individual"
            
            self.frames_metodos_entradas = {
                "Manual" : EntradaManual,
                "Extracción" : EntradaExtraccion
                }
            
            self.frames_opciones_resultado = {
                "Individual" : ResultadoIndividual,
                "Completo" : ResultadoCompleto
                }
            
            self.__class__._esta_inicializado = True
        
        
    def get_frame_entrada_de(self, nombre_vista:str) -> ctk.CTkFrame:
        if (nombre_vista != None and self._frame_calculadora != None):
            vista_principal = self.frames_metodos_entradas.get(nombre_vista)(self._frame_calculadora)
            return vista_principal
        else:
            raise ValueError("El nombre de la vista es inválido")

    def get_frame_resultado_de(self, nombre_vista:str) -> ctk.CTkFrame:
        if (nombre_vista != None and self._frame_opciones_resultado != None):
            vista_principal = self.frames_opciones_resultado.get(nombre_vista)(self._frame_opciones_resultado)
            return vista_principal
        else:
            raise ValueError("El nombre de la vista es inválido")

    def es_frame_entrada_seleccionado(self, nombre_frame: str) -> bool:
        if (nombre_frame != "" and nombre_frame != None):
            if (self._frame_entrada_seleccionado == nombre_frame):
                return True
            else:
                return False
        else:
            raise ValueError("El nombre de la vista es inválido")

    def es_frame_resultado_seleccionado(self, nombre_frame: str) -> bool:
        if (nombre_frame != "" and nombre_frame != None):
            if (self._frame_resultado_seleccionado == nombre_frame):
                return True
            else:
                return False
        else:
            raise ValueError("El nombre de la vista es inválido")

    def set_frame_calculadora(self, frame_calculadora:ctk.CTk) -> None:
        if (frame_calculadora != None):
            self._frame_calculadora = frame_calculadora
            
    def set_frame_opciones_resultado(self, frame_opciones_resultado:ctk.CTk) -> None:
        if (frame_opciones_resultado != None):
            self._frame_opciones_resultado = frame_opciones_resultado

    def cambiar_frame_entrada_a(self, nombre_frame:str) -> None:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.es_frame_entrada_seleccionado(nombre_frame)):
                return
            else:
                frame = self.get_frame_entrada_de(nombre_frame)
                self._frame_calculadora.cambiar_frame_metodo_entrada_a(frame)
                self._frame_entrada_seleccionado = nombre_frame
        else: 
            raise ValueError("Nombre del frame es inválido")
        
    def cambiar_frame_resultado_a(self, nombre_frame:str) -> None:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.es_frame_resultado_seleccionado(nombre_frame)):
                return
            else:
                frame = self.get_frame_resultado_de(nombre_frame)
                self._frame_opciones_resultado.cambiar_frame(frame)
                self._frame_resultado_seleccionado = nombre_frame
        else: 
            raise ValueError("Nombre del frame es inválido")
        