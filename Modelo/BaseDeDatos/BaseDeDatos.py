import json
import bcrypt
import os

class Usuario:
    def __init__(self, nombre, proyectos=None):
        self._nombre = nombre
        self._proyectos = proyectos or []  
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def proyectos(self):
        return self._proyectos

    @property
    def numero_proyectos(self):
        return len(self._proyectos)

    def agregar_proyecto(self, nombre_proyecto, proposiciones):
        nuevo_proyecto = Proyecto(nombre_proyecto, proposiciones)
        self._proyectos.append(nuevo_proyecto)


class Proyecto:
    def __init__(self, nombre, proposiciones):
        self._nombre = nombre
        self._proposiciones = proposiciones
    
    @property
    def nombre(self):
        return self._nombre

    @property
    def proposiciones(self):
        return self._proposiciones
    
    @property
    def numero_proposiciones(self):
        return len(self._proposiciones)


class BaseDeDatos:
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, RUTA=None):
        if not self.__class__._esta_inicializado:
            self.coordinador_datos = CoordinadorDatos(RUTA)
            self.coordinador_inicio_sesion = CoordinadorInicioSesion(self)
            self.coordinador_proyectos = CoordinadorProyectos(self)

            self.__class__._esta_inicializado = True

    def cargar_datos(self) -> dict:
        self.coordinador_datos.cargar_datos()

    def guardar_datos(self, datos:dict) -> None:
        self.coordinador_datos.guardar_datos(datos)
    
    def get_usuario(self, nombre):
        return self.coordinador_inicio_sesion.get_usuario(nombre)

    def registrar_usuario(self, nombre:str, contraseña:str) -> Usuario:
        return self.coordinador_inicio_sesion.registrar_usuario(nombre, contraseña)

    def iniciar_sesion(self, nombre, contraseña) -> Usuario:
        return self.coordinador_inicio_sesion.iniciar_sesion(nombre, contraseña)

    def guardar_proyecto(self, usuario:Usuario, nombre_proyecto:str, proposiciones:dict[str:str]) -> None:
        self.coordinador_proyectos.guardar_proyecto(usuario, nombre_proyecto, proposiciones)


import os
import json
import bcrypt
from typing import Dict, List, Optional, Any
import time

class CoordinadorDatos:
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, ruta: str):
        if not self.__class__._esta_inicializado:
            self.RUTA = ruta
            self.coordinador_inicio_sesion = CoordinadorInicioSesion(self)
            self.coordinador_proyectos = CoordinadorProyectos(self)
            self.__class__._esta_inicializado = True
    
    def cargar_datos(self) -> Dict[str, Any]:
        """Carga los datos del archivo JSON con validación de estructura"""
        try:
            if os.path.exists(self.RUTA):
                with open(self.RUTA, "r", encoding='utf-8') as archivo:
                    contenido = archivo.read().strip()
                    if contenido:
                        datos = json.loads(contenido)
                        if self._validar_estructura(datos):
                            return datos
        except (json.JSONDecodeError, IOError) as e:
            print(f"Advertencia: Error al cargar datos ({str(e)}). Se creará nueva estructura.")
        
        return self._crear_estructura_valida()
    
    def guardar_datos(self, datos: Dict[str, Any]) -> None:
        """Guarda los datos en el archivo JSON con manejo de errores"""
        try:
            with open(self.RUTA, "w", encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
        except IOError as e:
            raise RuntimeError(f"No se pudo guardar los datos: {str(e)}")
    
    def _validar_estructura(self, datos: Dict) -> bool:
        """Valida la estructura básica del diccionario de datos"""
        if not isinstance(datos, dict):
            return False
        if "usuarios" not in datos:
            return False
        if not isinstance(datos["usuarios"], list):
            return False
        return True
    
    def _crear_estructura_valida(self) -> Dict[str, List]:
        """Devuelve una estructura de datos nueva y válida"""
        return {"usuarios": []}


class CoordinadorInicioSesion:
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, base_de_datos: CoordinadorDatos):
        if not self.__class__._esta_inicializado:
            self.base_de_datos = base_de_datos
            self.__class__._esta_inicializado = True

    def registrar_usuario(self, nombre: str, contraseña: str) -> Optional[Usuario]:
        """Registra un nuevo usuario con contraseña hasheada"""
        datos = self.base_de_datos.cargar_datos()

        # Verificar si el usuario ya existe (comparación exacta)
        if any(u["nombre"] == nombre for u in datos["usuarios"]):
            return None

        # Hashear contraseña
        contraseña_hasheada = bcrypt.hashpw(contraseña.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

        # Crear nuevo usuario con estructura completa
        nuevo_usuario = {
            "nombre": nombre,
            "contraseña": contraseña_hasheada,
            "proyectos": []
        }
        
        datos["usuarios"].append(nuevo_usuario)
        self.base_de_datos.guardar_datos(datos)
        
        return Usuario(nombre, [])

    def iniciar_sesion(self, nombre: str, contraseña: str) -> Optional[Usuario]:
        """Autentica un usuario y devuelve su objeto Usuario con proyectos"""
        datos = self.base_de_datos.cargar_datos()

        for usuario_data in datos["usuarios"]:
            if usuario_data["nombre"] == nombre:
                try:
                    # Verificar contraseña
                    if bcrypt.checkpw(contraseña.encode("utf-8"), usuario_data["contraseña"].encode("utf-8")):
                        # Convertir proyectos a objetos Proyecto
                        proyectos = [
                            Proyecto(p["nombre"], p["proposiciones"]) 
                            for p in usuario_data.get("proyectos", [])
                            if isinstance(p, dict) and "nombre" in p and "proposiciones" in p
                        ]
                        return Usuario(nombre, proyectos)
                    return None
                except (UnicodeError, ValueError, AttributeError):
                    return None
        return None
    
    def get_usuario(self, nombre):
        datos = self.base_de_datos.cargar_datos()
        for usuario_data in datos["usuarios"]:
            if usuario_data["nombre"] == nombre:
                proyectos = [
                    Proyecto(p["nombre"], p["proposiciones"]) 
                    for p in usuario_data.get("proyectos", [])
                    if isinstance(p, dict) and "nombre" in p and "proposiciones" in p
                ]
                return Usuario(nombre, proyectos)


class CoordinadorProyectos:
    _instancia = None
    _esta_inicializado = False
    
    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia
    
    def __init__(self, base_de_datos: CoordinadorDatos):
        if not self.__class__._esta_inicializado:
            self.base_de_datos = base_de_datos
            self.__class__._esta_inicializado = True

    def guardar_proyecto(self, usuario: Usuario, nombre_proyecto: str, proposiciones: Dict[str, str]) -> None:
        """Guarda o actualiza un proyecto para un usuario existente"""
        MAX_INTENTOS = 3
        
        for intento in range(MAX_INTENTOS):
            try:
                datos = self.base_de_datos.cargar_datos()
                
                # Buscar usuario exacto
                usuario_data = next(
                    (u for u in datos["usuarios"] if u["nombre"] == usuario.nombre),
                    None
                )
                
                if not usuario_data:
                    raise ValueError(f"Usuario {usuario.nombre} no encontrado")
                
                # Inicializar proyectos si no existen
                if "proyectos" not in usuario_data:
                    usuario_data["proyectos"] = []
                
                # Buscar proyecto existente
                proyecto_existente = next(
                    (p for p in usuario_data["proyectos"] if p["nombre"] == nombre_proyecto),
                    None
                )
                
                if proyecto_existente:
                    # Actualizar proyecto existente
                    proyecto_existente["proposiciones"] = proposiciones
                else:
                    # Crear nuevo proyecto
                    usuario_data["proyectos"].append({
                        "nombre": nombre_proyecto,
                        "proposiciones": proposiciones
                    })
                
                self.base_de_datos.guardar_datos(datos)
                return
                
            except (json.JSONDecodeError, IOError) as e:
                if intento == MAX_INTENTOS - 1:
                    raise RuntimeError(f"Error al guardar proyecto después de {MAX_INTENTOS} intentos")
                time.sleep(0.1)
                continue
                
            except Exception as e:
                raise RuntimeError(f"Error inesperado: {str(e)}")

    def obtener_proyectos_usuario(self, nombre_usuario: str) -> List[Dict[str, Any]]:
        """Obtiene todos los proyectos de un usuario"""
        datos = self.base_de_datos.cargar_datos()
        
        for usuario in datos["usuarios"]:
            if usuario["nombre"] == nombre_usuario:
                return usuario.get("proyectos", [])
        
        return []
