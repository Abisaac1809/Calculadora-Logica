import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

class ToastAdvertencia(ctk.CTkToplevel):
    def __init__(self, master, mensaje="Ocurrió un error", duracion_segundos=3):
        super().__init__(master=master)
        self.geometry("300x80+650+10")
        self.overrideredirect(True) # Elimina barra superior y no permite que se mueva la ventana
        self.attributes("-topmost", True) # Mantiene esta ventana por encima de los demás
        self.configure(fg_color="#FFF3E0")
        self.mensaje = mensaje
        
        self.crear_widgets()
        self.insertar_widgets()
        
        self.destruir_despues_de(duracion_segundos)

    def crear_widgets(self):
        self.frame_principal = ctk.CTkFrame(
            master=self,
            fg_color="#FFF3E0"
            )
        
        imagen = Image.open("Vista//Materiales//warning.ico")
        imagen = imagen.resize((50, 50), Image.LANCZOS)
        self.icono = ImageTk.PhotoImage(imagen)
        self.icono_label = tk.Label(self.frame_principal, image=self.icon, bg="#FFF3E0")
        self.icon_label.pack(side="left", padx=(5, 10))
        
        self.label = tk.Label(
            self.frame_principal,
            text=self.mensaje,
            font=("Poppins", 20),
            fg="#BF360C", 
            bg="#FFF3E0",
    )
        
    def insertar_widgets(self):
        self.frame_principal.pack(expand=True, fill="both", padx=10, pady=10)
        self.label.pack(side="left", expand=True)
    
    def destruir_despues_de(self, duracion_en_segundos:int)->None:
        duracion_en_microsegundos = duracion_en_segundos * 1000
        self.after(duracion_en_microsegundos, self.destroy)
