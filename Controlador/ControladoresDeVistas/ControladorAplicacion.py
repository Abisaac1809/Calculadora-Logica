class ControladorFrameAplicacion():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, frame_aplicacion=None, vistas_aplicacion:dict=None):
        if not self.__class__._esta_inicializado:
            if (frame_aplicacion != None and vistas_aplicacion !=None): 
                self._frame_aplicacion = frame_aplicacion
                self._frame_seleccionado = "Inicio"
                self.vistas_aplicacion = vistas_aplicacion
                
                self.__class__._esta_inicializado = True
    
    def get_frame_de(self, nombre_frame:str):
        if (nombre_frame != "" and nombre_frame !=None):
            frame = self.vistas_aplicacion.get(nombre_frame)
            return frame
        else:
            raise ValueError("Nombre del frame es inválido")
    
    def cambiar_frame_aplicacion_a(self, nombre_frame:str) -> None:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.frame_seleccionado_es(nombre_frame)):
                return
            else:
                frame = self.get_frame_de(nombre_frame)
                self._frame_aplicacion.cambiar_frame_a(frame)
                self._frame_seleccionado = nombre_frame
        else: 
            raise ValueError("Nombre del frame es inválido")
    
    def frame_seleccionado_es(self, nombre_frame:str) -> bool:
        if (nombre_frame != None):
            if (nombre_frame == self._frame_seleccionado):
                return True
            else: 
                return False
        else:
            raise ValueError("Nombre de frame inválido")
        
    def actualizar_proyectos_inicio(self):
        frame = self.get_frame_de("Inicio")
        frame.actualizar_proyectos_inicio()