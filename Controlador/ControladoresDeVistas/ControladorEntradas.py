from Controlador.ControladoresDeVistas.ControladorAplicacion import *

class ControladorEntradas():
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, frame_entrada=None, vistas_entrada:dict=None):
        if not self.__class__._esta_inicializado:
            if (frame_entrada != None and vistas_entrada != None):
                
                self._frame_entrada = frame_entrada
                self.vistas_entradas = vistas_entrada
                self.nombre_tipo_entrada_seleccionada = "Manual"
                
                self.__class__._esta_inicializado = True
    
    def get_nombre_tipo_entrada_seleccionada(self) -> str:
        return self.nombre_tipo_entrada_seleccionada
    
    def get_frame_de(self, nombre_vista:str):
        if (nombre_vista != None and nombre_vista !=""):
            vista_seleccionada = self.vistas_entradas.get(nombre_vista)
            return vista_seleccionada
        else:
            raise ValueError("El nombre de la vista es inválido")
    
    def get_diccionario_proposiciones_manuales(self):
        frame_entrada_manual = self.get_frame_de("Manual")
        proposiciones = frame_entrada_manual.get_lista_proposiciones()
        diccionario_de_proposiciones = {}
        
        for proposicion in proposiciones:
            nombre = proposicion.get_nombre()
            proposicion_texto = proposicion.get_proposicion()
            diccionario_de_proposiciones[nombre] = proposicion_texto
        
        return diccionario_de_proposiciones
    
    def borrar_todas_las_proposiciones_manuales(self):
        frame_entrada_manual = self.get_frame_de("Manual")
        frame_entrada_manual.borrar_todas_las_proposiciones()
    
    def frame_seleccionado_es(self, nombre_frame: str) -> bool:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.nombre_tipo_entrada_seleccionada == nombre_frame):
                return True
            else:
                return False
        else:
            raise ValueError("El nombre de la vista es inválido")
    
    def cambiar_frame_a(self, nombre_frame:str) -> None:
        if (nombre_frame != "" and nombre_frame != None):
            if (self.frame_seleccionado_es(nombre_frame)):
                return
            else:
                frame = self.get_frame_de(nombre_frame)
                self._frame_entrada.cambiar_frame_a(frame)
                if (nombre_frame == "Manual"):
                    self.reducir_entrada_frame()
                else:
                    self.agrandar_entrada_frame()
                self.nombre_tipo_entrada_seleccionada = nombre_frame
        else: 
            raise ValueError("Nombre del frame es inválido")
    
    def agrandar_entrada_frame(self):
        controlador_aplicacion = ControladorFrameAplicacion()
        frame_calculadora = controlador_aplicacion.get_frame_de("Calculadora Lógica")
        frame_calculadora.agrandar_entrada_frame()
    
    def reducir_entrada_frame(self):
        controlador_aplicacion = ControladorFrameAplicacion()
        frame_calculadora = controlador_aplicacion.get_frame_de("Calculadora Lógica")
        frame_calculadora.reducir_entrada_frame()
