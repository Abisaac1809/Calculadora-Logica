import customtkinter as ctk

from Controlador.ControladoresDeVistas.ControladorVistaPrincipal import ControladorVista

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("Vista//Materiales//tema.json")
        self.title("VeriLogic")
        self.iconbitmap("Vista//Materiales//logicIcon.ico")
        self.geometry("1500x700+0+0")
        
        self.controlador_vista = ControladorVista()
        self.controlador_vista.set_root_principal(self)
        
        self._frame_actual = None #self.controlador_vista.get_vista_principal_de("Inicio Sesion")
        
        # Eliminar después de pruebas
        self.set_frame_actual("Aplicacion")
        
    def set_frame_actual(self, nombre_frame:str) -> None:
        if (nombre_frame != None):
            
            if self._frame_actual != None:
                self._frame_actual.destroy()
                
            self._frame_actual = self.controlador_vista.get_vista_principal_de(nombre_frame)
            self._frame_actual.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
        else:
            raise ValueError("No se ha encontrado el frame")