import customtkinter as ctk
from Vista.Resultado.Componentes.ctktable import *
from Vista.Resultado.VentanaNombre import *

class ResultadosScrolleable(ctk.CTkScrollableFrame):
    def __init__(self, master, resultados:list, controlador, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F5F7FA")
        if resultados == None:
            self.destroy()
        self.resultados = resultados
        self.controlador_vista_principal = controlador
        
        self.crear_widgets()
        self.configurar_widgets()
        self.insertar_widgets()
    
    def crear_frames_resultados(self)->list[ctk.CTkFrame]:
        if (self.resultados != None):
            lista_de_frames_resultado = []
            for resultado in self.resultados:
                frame_resultado = ResultadoFrame(self, resultado)
                lista_de_frames_resultado.append(frame_resultado)
            return lista_de_frames_resultado
        else:
            raise ValueError("La lista de resultados es nula")
    
    def crear_widgets(self):
        self.titulo_label = ctk.CTkLabel(
            master=self,
            text="Resultados",
            text_color="#121212",
            font=("Poppins", 80, "bold"), 
            anchor="w"
        )
        
        self.frames_resultados = self.crear_frames_resultados()
        
        self.frame_de_botones = ctk.CTkFrame(self, fg_color="transparent")
        
        self.boton_volver = ctk.CTkButton(
            master=self.frame_de_botones,
            fg_color="#388E3C",
            text_color="#FFFFFF",
            text="Volver",
            font=("Poppins", 25),
            )
        
        self.boton_guardar = ctk.CTkButton(
            master=self.frame_de_botones,
            fg_color="#388E3C",
            text_color="#FFFFFF",
            text="Guardar",
            font=("Poppins", 25)
            )
    
    def configurar_widgets(self):
        self.boton_volver.bind("<Button-1>", self.volver)
        self.boton_guardar.bind("<Button-1>", self.guardar)
    
    def insertar_widgets(self):
        self.titulo_label.pack(fill="x", padx=60, pady=10)
        for frame_resultado in self.frames_resultados:
            frame_resultado.pack(expand=True, fill="both", pady=(30,100))
        
        self.boton_volver.pack(side="left", expand=True, fill="both", padx=10, pady=10, ipady=20)
        self.boton_guardar.pack(side="left", expand=True, fill="both", padx=10, pady=10, ipady=20)
        self.frame_de_botones.pack(fill="x", pady=20, padx=500)
    
    def volver(self, evento):
        self.destroy()
        self.controlador_vista_principal.set_vista_seleccionada("Aplicacion")
        self.controlador_vista_principal.volver_frame_aplicacion()
    
    def guardar(self, evento):
        ventana =VentanaNombre(self, self.resultados[-1]["Proposiciones"])
        ventana.wait_window()
        self.controlador_vista_principal.volver_frame_aplicacion()


class ResultadoFrame(ctk.CTkFrame):
    def __init__(self, master, resultado:dict, **kwargs):
        super().__init__(master=master)
        self.configure(fg_color="#F5F7FA")
        self.proposiciones = resultado.get("Proposiciones")
        self.formula = resultado.get("Formula")
        self.texto_lenguaje_natural = resultado.get("Texto")
        self.matriz_tabla_verdad = resultado.get("Tabla")
        
        self.crear_widgets()
        self.insertar_widgets()
    
    def crear_widgets(self):
        self.proposiciones_titulo_label = Titulo(self, "Proposiciones")
        
        self.proposiciones_labels = self.crear_labels_proposiciones(self.proposiciones)
        
        self.formula_titulo_label = Titulo(self, "Fórmula")
        
        self.formula_label = Texto(self, self.formula)
        
        self.texto_titulo_label = Titulo(self, "Texto")
        
        self.texto_label = Texto(self, self.texto_lenguaje_natural)
        
        self.tabla_titulo_label = Titulo(self, "Tabla de verdad")
        
        self.tabla_verdad = CTkTable(
            master=self,
            values=self.matriz_tabla_verdad,
            font=("Poppins", 20),
            text_color="#555555",
            header_color="#E8F5E9",border_width=1,
            border_color="#2b2b2b",
            fg_color="black"
            )

    def insertar_widgets(self):
        self.proposiciones_titulo_label.pack(fill="x", padx=60, pady=10)
        [label.pack(fill="x", padx=60) for label in self.proposiciones_labels]
        self.formula_titulo_label.pack(fill="x", padx=60, pady=10)
        self.formula_label.pack(fill="x", padx=60, pady=10)
        
        if (self.texto_lenguaje_natural != None):
            self.texto_titulo_label.pack(fill="x", padx=60, pady=10)
            self.texto_label.pack(fill="x", padx=60, pady=10)
        
        if (self.matriz_tabla_verdad != None):
            self.tabla_titulo_label.pack(fill="x", padx=60, pady=10)
            self.tabla_verdad.pack(expand=True, fill="both", padx=60)
    
    def crear_labels_proposiciones(self, proposiciones:dict):
        if (proposiciones != None):
            labels_proposiciones = []
            for nombre, proposicion in proposiciones.items():
                nueva_label = Texto(self, f"{nombre} = {proposicion}")
                labels_proposiciones.append(nueva_label)
            return labels_proposiciones
        else:
            raise ValueError("Resultado es inválido")


class Titulo(ctk.CTkLabel):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master=master)
        if (texto != None):
            self.configure(
                text=texto,
                text_color="#333333",
                font=("Poppins", 45),
                anchor="w"
                )
        else:
            self.destroy()


class Texto(ctk.CTkLabel):
    def __init__(self, master, texto, **kwargs):
        super().__init__(master=master)
        if (texto != None):
            self.configure(
                text=texto,
                text_color="#555555",
                font=("Poppins", 20),
                anchor="w"
            )
        else:
            self.destroy()