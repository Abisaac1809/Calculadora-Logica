import json
import os
from typing import Dict, Any

class ConfigManager:
    """Manejador de configuraciones en archivo JSON"""
    
    def __init__(self):
        self.config_path = "Modelo//Configuracion//configuracion.json"
        self.default_config = {
            "min_proposiciones": 4,
        }
    
    def cargar_config(self) -> Dict[str, Any]:
        """Carga las configuraciones desde el archivo JSON"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, "r", encoding='utf-8') as f:
                    config = json.load(f)
                    # Validar estructura básica
                    if isinstance(config, dict):
                        return {**self.default_config, **config}  # Fusiona con valores por defecto
        except (json.JSONDecodeError, IOError):
            pass
        return self.default_config.copy()
    
    def guardar_config(self, config: Dict[str, Any]) -> bool:
        """Guarda las configuraciones en el archivo JSON"""
        try:
            with open(self.config_path, "w", encoding='utf-8') as f:
                json.dump(config, f, indent=4, ensure_ascii=False)
            return True
        except IOError:
            return False
