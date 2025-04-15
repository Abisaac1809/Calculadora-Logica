import customtkinter as ctk

class FrameTexto(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        
        self.crear_widgets()
        self.insertar_widgets()
        
    def crear_widgets(self):
        self.bienvenido_label = ctk.CTkLabel(
            master=self,
            text="Buenos días, Abisaac",
            text_color="#2e2e2c",
            font=("Poppins", 60, "bold"), 
            anchor="w"
        )
    
        self.frase_label = ctk.CTkLabel(
            master=self,
            text="La lógica no es solo reglas, es el arte de pensar con claridad",
            font=("Poppins", 20),
            text_color="gray",
            anchor="w"
        )
        
        self.numero_de_proyectos_label = ctk.CTkLabel(
            master=self,
            text="Proyectos totales\n2",
            text_color="#2e2e2c",
            font=("Poppins", 30, "bold")
            )   
    
    def insertar_widgets(self):
        self.bienvenido_label.place(relx=0.02, rely=0.0, relheight=0.7) 
        self.frase_label.place(relx=0.02, rely=0.55, relwidth=0.7, relheight=0.3)
        self.numero_de_proyectos_label.place(relx=0.65,rely=0.2, relwidth=0.2, relheight=0.6)