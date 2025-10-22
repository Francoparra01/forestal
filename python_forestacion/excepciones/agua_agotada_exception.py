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