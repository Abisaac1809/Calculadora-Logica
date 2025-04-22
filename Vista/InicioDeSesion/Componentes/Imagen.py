import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

class Imagen(ctk.CTkFrame):
    def __init__(self, padre):
        super().__init__(master=padre, fg_color="transparent")
        self.imagen = Image.open("Vista//Materiales//logica.jpg")
        self.canvas_imagen = tk.Canvas(self, bd=0, highlightthickness=0, relief="ridge")
        self.canvas_imagen.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.canvas_imagen.bind("<Configure>", self.dimencionar_imagen)

    def dimencionar_imagen(self, event):
        width = event.width
        height = event.height
        
        self.resized_image = self.imagen.resize((width, height))
        self.resized_tk = ImageTk.PhotoImage(self.resized_image)
        
        self.canvas_imagen.create_image(0,0, image=self.resized_tk, anchor="nw")