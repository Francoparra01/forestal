"""
Interfaz base para todos los cultivos del sistema.
"""

from abc import ABC


class Cultivo(ABC):
    """
    Clase abstracta base para todos los cultivos.
    
    Attributes:
        _agua: Cantidad de agua en litros
        _superficie: Superficie ocupada en metros cuadrados
    """
    
    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie que ocupa en m2
        """
        self._agua = agua
        self._superficie = superficie
    
    def get_agua(self) -> int:
        """Retorna cantidad de agua del cultivo."""
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """Establece cantidad de agua del cultivo."""
        self._agua = agua
    
    def get_superficie(self) -> float:
        """Retorna superficie ocupada por el cultivo."""
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """Establece superficie del cultivo."""
        self._superficie = superficie