"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/excepciones
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 6
"""

# ================================================================================
# ARCHIVO 1/6: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/excepciones/__init__.py
# ================================================================================

"""
Excepciones personalizadas del sistema.
"""

# ================================================================================
# ARCHIVO 2/6: agua_agotada_exception.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/excepciones/agua_agotada_exception.py
# ================================================================================

"""
Excepción cuando no hay agua suficiente.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_AGUA_AGOTADA_USER,
    MSG_AGUA_AGOTADA_TECH
)


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay agua disponible.
    
    Attributes:
        _agua_requerida: Agua necesaria
        _agua_disponible: Agua disponible actual
    """
    
    def __init__(self, agua_requerida: int, agua_disponible: int):
        """
        Inicializa la excepción.
        
        Args:
            agua_requerida: Agua necesaria en litros
            agua_disponible: Agua disponible en litros
        """
        user_msg = MSG_AGUA_AGOTADA_USER
        tech_msg = (
            f"{MSG_AGUA_AGOTADA_TECH}: "
            f"requerida={agua_requerida}L, disponible={agua_disponible}L"
        )
        super().__init__(user_msg, tech_msg)
        
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible
    
    def get_agua_requerida(self) -> int:
        """Retorna agua requerida."""
        return self._agua_requerida
    
    def get_agua_disponible(self) -> int:
        """Retorna agua disponible."""
        return self._agua_disponible

# ================================================================================
# ARCHIVO 3/6: forestacion_exception.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/excepciones/forestacion_exception.py
# ================================================================================

"""
Excepción base del sistema.
"""


class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del dominio.
    
    Attributes:
        _user_message: Mensaje amigable para usuario
        _technical_message: Mensaje técnico para desarrollador
    """
    
    def __init__(self, user_message: str, technical_message: str):
        """
        Inicializa la excepción.
        
        Args:
            user_message: Mensaje para usuario final
            technical_message: Mensaje técnico detallado
        """
        super().__init__(user_message)
        self._user_message = user_message
        self._technical_message = technical_message
    
    def get_user_message(self) -> str:
        """Retorna mensaje amigable."""
        return self._user_message
    
    def get_technical_message(self) -> str:
        """Retorna mensaje técnico."""
        return self._technical_message
    
    def get_full_message(self) -> str:
        """Retorna mensaje completo."""
        return f"{self._user_message}\nDetalles tecnicos: {self._technical_message}"

# ================================================================================
# ARCHIVO 4/6: mensajes_exception.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/excepciones/mensajes_exception.py
# ================================================================================

"""
Mensajes centralizados para excepciones.
"""

# Mensajes de SuperficieInsuficienteException
MSG_SUPERFICIE_INSUFICIENTE_USER = "No hay suficiente superficie disponible para plantar"
MSG_SUPERFICIE_INSUFICIENTE_TECH = "Superficie requerida excede disponible"

# Mensajes de AguaAgotadaException
MSG_AGUA_AGOTADA_USER = "No hay suficiente agua disponible para regar"
MSG_AGUA_AGOTADA_TECH = "Agua requerida excede disponible"

# Mensajes de PersistenciaException
MSG_PERSISTENCIA_ERROR_USER = "Error al guardar o recuperar datos"
MSG_PERSISTENCIA_ERROR_TECH = "Fallo en operacion de serializacion"

# ================================================================================
# ARCHIVO 5/6: persistencia_exception.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/excepciones/persistencia_exception.py
# ================================================================================

"""
Excepción de errores de persistencia.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_PERSISTENCIA_ERROR_USER,
    MSG_PERSISTENCIA_ERROR_TECH
)


class PersistenciaException(ForestacionException):
    """
    Excepción lanzada en errores de persistencia.
    """
    
    def __init__(self, detalle: str):
        """
        Inicializa la excepción.
        
        Args:
            detalle: Detalle del error
        """
        user_msg = MSG_PERSISTENCIA_ERROR_USER
        tech_msg = f"{MSG_PERSISTENCIA_ERROR_TECH}: {detalle}"
        super().__init__(user_msg, tech_msg)

# ================================================================================
# ARCHIVO 6/6: superficie_insuficiente_exception.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ================================================================================

"""
Excepción cuando no hay superficie suficiente.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INSUFICIENTE_USER,
    MSG_SUPERFICIE_INSUFICIENTE_TECH
)


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay superficie disponible.
    
    Attributes:
        _superficie_requerida: Superficie necesaria
        _superficie_disponible: Superficie disponible actual
    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa la excepción.
        
        Args:
            superficie_requerida: Superficie necesaria en m2
            superficie_disponible: Superficie disponible en m2
        """
        user_msg = MSG_SUPERFICIE_INSUFICIENTE_USER
        tech_msg = (
            f"{MSG_SUPERFICIE_INSUFICIENTE_TECH}: "
            f"requerida={superficie_requerida}, disponible={superficie_disponible}"
        )
        super().__init__(user_msg, tech_msg)
        
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
    
    def get_superficie_requerida(self) -> float:
        """Retorna superficie requerida."""
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible

