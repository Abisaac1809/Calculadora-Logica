import sys

from Vista.InicioDeSesion.Componentes.Menu import *
from Vista.InicioDeSesion.Componentes.Imagen import *
from Controlador.ControladoresDeInicioSesion.ControladorInicioSesion import *

class InicioDeSesionFrame(ctk.CTkFrame):
    def __init__(self, padre):
        super().__init__(master=padre)
        self.controlador = ControladorInicioSesion()
        self.menu = Menu(self)
        self.imagen = Imagen(self)
        self.menu.place(relx=0.0, rely=0.0, relwidth=0.4, relheight=1)
        self.imagen.place(relx=0.4, rely=0.0, relwidth=0.6, relheight=1)