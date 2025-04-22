import customtkinter as ctk
from Modelo.Configuracion.GestionadorDelaConfiguracion import *

class ConfigFrame(ctk.CTkFrame):
    """Frame de configuración del programa"""
    
    def __init__(self, master, config_manager: ConfigManager, **kwargs):
        super().__init__(master, **kwargs)
        self.config_manager = config_manager
        self.config = self.config_manager.cargar_config()
        
        self.configure(fg_color="#F9FAFB", corner_radius=10)
        self._crear_widgets()
        self._colocar_widgets()
        self._configurar_eventos()
    
    def _crear_widgets(self):
        """Crea todos los widgets del frame"""
        # Título principal
        self.titulo = ctk.CTkLabel(
            self,
            text="Configuraciones",
            font=("Poppins", 24, "bold"),
            text_color="#2E3440"
        )
        
        # Frame para las configuraciones
        self.config_container = ctk.CTkFrame(self, fg_color="transparent")
        
        # Configuración de mínimo de proposiciones
        self.min_prop_label = ctk.CTkLabel(
            self.config_container,
            text="Número mínimo de proposiciones:",
            font=("Poppins", 14),
            text_color="#4C566A"
        )
        
        self.min_prop_entry = ctk.CTkEntry(
            self.config_container,
            font=("Poppins", 14),
            width=100,
            justify="center"
        )
        self.min_prop_entry.insert(0, str(self.config["min_proposiciones"]))
        
        # Botón de guardar
        self.guardar_btn = ctk.CTkButton(
            self,
            text="Guardar Configuración",
            font=("Poppins", 14, "bold"),
            fg_color="#4C566A",
            hover_color="#3B4252",
            command=self._guardar_configuracion
        )
    
    def _colocar_widgets(self):
        """Organiza los widgets en el frame"""
        self.titulo.pack(pady=(20, 30))
        self.config_container.pack(fill="x", padx=20)
        
        # Grid para las configuraciones
        self.min_prop_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.min_prop_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        
        self.guardar_btn.pack(pady=30)
    
    def _configurar_eventos(self):
        """Configura los eventos de los widgets"""
        # Validar que solo se ingresen números
        def validar_entrada(texto: str) -> bool:
            if texto.isdigit() or texto == "":
                return True
            return False
        
        vcmd = (self.register(validar_entrada), '%P')
        self.min_prop_entry.configure(validate="key", validatecommand=vcmd)
    
    def _guardar_configuracion(self):
        """Guarda las configuraciones modificadas"""
        try:
            print("h")
            min_prop = int(self.min_prop_entry.get())
            if min_prop < 1:
                raise ValueError("El valor debe ser mayor a 0")
            
            self.config["min_proposiciones"] = min_prop
            self.config_manager.guardar_config(self.config)
            
        
        except ValueError as e:
            self.min_prop_entry.delete(0, "end")
            self.min_prop_entry.insert(0, str(self.config["min_proposiciones"]))
        

