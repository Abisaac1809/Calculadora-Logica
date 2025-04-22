import customtkinter as ctk
from tkinter import messagebox
import re
from Controlador.ControladoresDeUsuario.ControladorDeUsuario import *
from Controlador.ControladoresDeVistas.ControladorAplicacion import *


class VentanaNombre(ctk.CTkToplevel):
    def __init__(self, parent, proposiciones):
        super().__init__(parent)
        self.proposiciones = proposiciones
        self.resultado = None  # Variable para almacenar el resultado
        self.controlador_de_usuario = ControladorDeUsuario()

        self.title("Guardar Proyecto")
        self.geometry("400x200")
        self.resizable(False, False)

        # Etiqueta
        label = ctk.CTkLabel(self, text="Inserte el nombre de su proyecto", font=("Poppins", 20))
        label.pack(pady=10)

        # Entrada
        self.nombre_entry = ctk.CTkEntry(
            self, placeholder_text="Nombre del proyecto", width=300,font=("Poppins", 15))
        self.nombre_entry.pack(pady=5)
        self.nombre_entry.focus_set()  # Hacer foco en la entrada

        # Botones
        botones_frame = ctk.CTkFrame(self)
        botones_frame.pack(pady=20)

        guardar_btn = ctk.CTkButton(
            botones_frame, text="Guardar", command=self.guardar_proyecto,font=("Poppins", 18))
        guardar_btn.pack(side="right", padx=10)

        cancelar_btn = ctk.CTkButton(
            botones_frame, text="Cancelar", command=self.cancelar,font=("Poppins", 18))
        cancelar_btn.pack(side="left", padx=10)

    def validar_nombre(self, nombre):
        return bool(re.fullmatch(r"[a-zA-Z0-9]+", nombre))

    def guardar_proyecto(self):
        controlador = ControladorFrameAplicacion()
        nombre = self.nombre_entry.get()
        if self.validar_nombre(nombre):
            self.controlador_de_usuario.agregar_nuevo_proyecto(nombre, self.proposiciones)
            self.destroy()
            controlador.actualizar_proyectos_inicio()
        else:
            messagebox.showerror("Error", "El nombre solo debe contener letras y números.")

    def cancelar(self):
        """Acción del botón Cancelar."""
        self.resultado = None
        self.destroy()
