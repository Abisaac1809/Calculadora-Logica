import customtkinter as ctk

class ResultadoCompleto(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()

    def crear_widgets(self):
        self.titulo_label = ctk.CTkLabel(
            master=self,
            text="Generar",
            font=("Poppins", 25, "bold")
            )
        
        self.conjuncion_opcion = ctk.CTkCheckBox(
            master=self,
            text="Conjuncion",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )
    
        self.disyuncion_opcion = ctk.CTkCheckBox(
            master=self,
            text="Disyuncion",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )
        
        self.condicional_opcion = ctk.CTkCheckBox(
            master=self,
            text="Conjuncion",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )
        
        self.bicondicional_opcion = ctk.CTkCheckBox(
            master=self,
            text="Bicondicional",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )

        self.negacion_opcion = ctk.CTkCheckBox(
            master=self,
            text="Negación",
            font=("Poppins", 20),
            onvalue=1,
            offvalue=0
            )

    
    def configurar_widgets(self):
        pass

    def insertar_widgets(self):
        self.titulo_label.pack(expand= True, fill="both", pady=10, padx=10)
        self.conjuncion_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.disyuncion_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.condicional_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.bicondicional_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.negacion_opcion.pack(expand= True, fill="both", pady=(10,40), padx=50)