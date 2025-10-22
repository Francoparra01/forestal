"""
Entidad Lechuga - Hortaliza de hoja.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA


class Lechuga(Hortaliza):
    """
    Representa una lechuga.
    
    Attributes:
        _variedad: Variedad de lechuga (Criolla, Romana, Mantecosa)
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa una Lechuga.
        
        Args:
            variedad: Variedad de lechuga
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """Retorna variedad de lechuga."""
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """Establece variedad de lechuga."""
        self._variedad = variedad