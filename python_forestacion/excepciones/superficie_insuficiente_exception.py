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