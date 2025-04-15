from Vista.Aplicacion.FrameAplicacion import *

class ControladorVista():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self):
        if not self.__class__._esta_inicializado: 
            self._root_principal = None
            
            self.vistas_principales = {
                "Inicio Sesion": 1,
                "Aplicacion": FrameAplicacion
                }
            self.__class__._esta_inicializado = True
        
        
    def get_vista_principal_de(self, nombre_vista:str) -> ctk.CTkFrame:
        if (nombre_vista != None and self._root_principal != None):
            vista_principal = self.vistas_principales.get(nombre_vista)(self._root_principal)
            return vista_principal
        else:
            raise ValueError("No se ha encontrado la vista")
    
    def set_root_principal(self, root_principal:ctk.CTk) -> None:
        if (root_principal != None):
            self._root_principal = root_principal