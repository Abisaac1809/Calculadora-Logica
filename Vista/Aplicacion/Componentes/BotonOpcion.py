import customtkinter as ctk

class BotonOpcion(ctk.CTkButton):
    def __init__(self, master:ctk.CTkFrame, texto:str, **kwargs):
        super().__init__(master=master)
        
        self.configure(
            text=texto,
            font=("Poppins", 30, "bold"),
            fg_color="transparent",  
            text_color="#424242",  
            hover_color="#e0e0e0",  
            corner_radius=0
            )