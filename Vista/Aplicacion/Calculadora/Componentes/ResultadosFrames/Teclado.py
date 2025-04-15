import customtkinter as ctk

class Teclado(ctk.CTkFrame):
    def __init__(self, master, entry):
        super().__init__(master=master, fg_color="transparent")
        self.master = master
        self.entry = entry
        self.rowconfigure((0,1), weight=1)
        self.columnconfigure((0,1,2,3), weight=1)
        
        self.crear_widgets()
        # self.configurar_widgets()
        self.grid_widgets()

    def crear_widgets(self):
        self.boton_disyuncion = Boton(self, "∧", self.entry, True)
        self.boton_conjuncion = Boton(self, "∨", self.entry, True)
        self.boton_condicional = Boton(self, "→", self.entry, True)
        self.boton_bicondicional = Boton(self, "↔", self.entry, True)
        self.boton_negacion = Boton(self, "¬", self.entry, True)
        self.boton_parentesis_abre = Boton(self, "(", self.entry, True)
        self.boton_parentesis_cierra = Boton(self, ")", self.entry, True)
        self.boton_borrar = Boton(self, "AC", self.entry, False)
    
    def configurar_widgets(self):
        self.boton_borrar.bind("<Button-1>", lambda e: self.entry.delete(0, "end"))
        self.entry.bind("<Return>", self.realizar_operacion)

    def grid_widgets(self):
        self.boton_disyuncion.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        self.boton_conjuncion.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)
        self.boton_condicional.grid(row=0, column=2, sticky="nswe", padx=5, pady=5)
        self.boton_bicondicional.grid(row=0, column=3, sticky="nswe", padx=5, pady=5)
        self.boton_negacion.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
        self.boton_parentesis_abre.grid(row=1, column=1, sticky="nswe", padx=5, pady=5)
        self.boton_parentesis_cierra.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)
        self.boton_borrar.grid(row=1, column=3, sticky="nswe", padx=5, pady=5)

    def realizar_operacion(self, evento):
        operacion = self.entry.get()
        self.entry.delete(0, "end")
        self.controlador.realizar_operacion(operacion, self.label)

class Boton(ctk.CTkButton):
    def __init__(self, master, signo, entry, puede_escribir):
        super().__init__(master=master)
        self.entry = entry
        self.configure(
            fg_color="#388E3C",
            font=("Poppins", 25),
            text=signo,
            text_color="#FFFFFF",
            corner_radius=20,
            hover_color="#2E7D32"
            )
        if (puede_escribir): self.configure(command=self.escribir)
    
    def escribir(self):
        texto_escrito = self.entry.get()
        self.entry.delete(0, "end")
        self.entry.insert(0, (texto_escrito + self._text))