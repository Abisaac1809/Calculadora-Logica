import customtkinter as ctk

class ResultadoCompleto(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="transparent")
        
        self.se_debe_hacer_conjuncion = ctk.BooleanVar(value=True)
        self.se_debe_hacer_disyuncion = ctk.BooleanVar(value=True)
        self.se_debe_hacer_condicional = ctk.BooleanVar(value=True)
        self.se_debe_hacer_bicondicional = ctk.BooleanVar(value=True)
        
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
            onvalue=True,
            offvalue=False,
            variable=self.se_debe_hacer_conjuncion
            )
    
        self.disyuncion_opcion = ctk.CTkCheckBox(
            master=self,
            text="Disyuncion",
            font=("Poppins", 20),
            onvalue=True,
            offvalue=False,
            variable=self.se_debe_hacer_disyuncion
            )
        
        self.condicional_opcion = ctk.CTkCheckBox(
            master=self,
            text="Conjuncion",
            font=("Poppins", 20),
            onvalue=True,
            offvalue=False,
            variable=self.se_debe_hacer_condicional
            )
        
        self.bicondicional_opcion = ctk.CTkCheckBox(
            master=self,
            text="Bicondicional",
            font=("Poppins", 20),
            onvalue=True,
            offvalue=False,
            variable=self.se_debe_hacer_bicondicional
            )
    
    def configurar_widgets(self):
        pass

    def insertar_widgets(self):
        self.titulo_label.pack(expand= True, fill="both", pady=10, padx=10)
        self.conjuncion_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.disyuncion_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.condicional_opcion.pack(expand= True, fill="both", pady=10, padx=50)
        self.bicondicional_opcion.pack(expand= True, fill="both", pady=10, padx=50)
    
    def get_nombre_formulas_que_se_deben_hacer(self):
        nombres_formulas_que_se_deben_hacer = []
        
        if self.se_debe_hacer_conjuncion.get():
            nombres_formulas_que_se_deben_hacer.append("Conjuncion")
            
        if self.se_debe_hacer_disyuncion.get():
            nombres_formulas_que_se_deben_hacer.append("Disyuncion")
            
        if self.se_debe_hacer_condicional.get():
            nombres_formulas_que_se_deben_hacer.append("Condicional")
            
        if self.se_debe_hacer_bicondicional.get():
            nombres_formulas_que_se_deben_hacer.append("Bicondicional")
        
        return nombres_formulas_que_se_deben_hacer