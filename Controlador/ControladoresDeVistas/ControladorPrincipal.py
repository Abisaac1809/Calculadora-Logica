from Vista.Aplicacion.Componentes.ToastAdvertencia import *
from Vista.Resultado.FrameResultado import ResultadosScrolleable

class ControladorVistaPrincipal():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, root_principal=None, vistas_principales=None):
        if not self.__class__._esta_inicializado: 
            if root_principal and vistas_principales:
                self._root_principal = root_principal
                self._vista_seleccionada = "Aplicacion"
                
                self.vistas_principales = vistas_principales
                self.__class__._esta_inicializado = True
        
    def get_vista_principal_de(self, nombre_vista:str) -> ctk.CTkFrame:
        if (nombre_vista != None and self._root_principal != None):
            vista_principal = self.vistas_principales.get(nombre_vista)
            return vista_principal
        else:
            raise ValueError("No se ha encontrado la vista")
    
    def vista_seleccionada_es(self, nombre_vista:str) -> bool:
        if (nombre_vista != "" and nombre_vista != None):
            if (nombre_vista == self._vista_seleccionada):
                return True
            else:
                return False
        else:
            raise ValueError("El nombre de la vista es inválido")
    
    def cambiar_vista_a(self, nombre_vista:str) -> None:
        if (nombre_vista != "" and nombre_vista != None):
            if (self._vista_seleccionada == nombre_vista):
                return
            else:
                vista = self.get_vista_principal_de(nombre_vista)
                self._root_principal.cambiar_frame_a(vista)
                self._vista_seleccionada = nombre_vista
        else:
            raise ValueError("El nombre de la vista es inválido")
    
    def mostrar_resultado(self, resultados:list[dict]):
        if (resultados != None):
            frame_resultado = ResultadosScrolleable(self._root_principal, resultados, self)
            self._root_principal.cambiar_frame_a(frame_resultado)
            self._vista_seleccionada = "Resultado"
        else: 
            raise ValueError("Los resultados son inválidos")
        
    def mostrar_advertencia(self, mensaje:str, duracion_en_segundos:int=2)->None:
        if (mensaje != None and duracion_en_segundos > 0):
            ToastAdvertencia(self._root_principal, mensaje, duracion_en_segundos)
        else:
            raise ValueError("Mensaje y duración inválidos")
