from Vista.Aplicacion.FrameAplicacion import *
#from Vista.Aplicacion.Componentes.ToastAdvertencia import *

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
                
                self.vistas_principales = vistas_principales
                self.__class__._esta_inicializado = True
        
        
    def get_vista_principal_de(self, nombre_vista:str) -> ctk.CTkFrame:
        if (nombre_vista != None and self._root_principal != None):
            vista_principal = self.vistas_principales.get(nombre_vista)
            return vista_principal
        else:
            raise ValueError("No se ha encontrado la vista")
    
    """
    def mostrar_advertencia(self, mensaje:str, duracion_en_segundos:int)->None:
        if (mensaje != None and duracion_en_segundos > 0):
            ToastAdvertencia(self._root_principal, mensaje, duracion_en_segundos)
        else:
            raise ValueError("Mensaje y duración inválidos")
    """