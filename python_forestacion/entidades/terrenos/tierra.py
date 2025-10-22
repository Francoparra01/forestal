"""
Entidad Tierra - Parcela catastral.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Representa una parcela de tierra catastral.
    
    Attributes:
        _padron: Número de padrón catastral único
        _superficie: Superficie en metros cuadrados
        _domicilio: Ubicación geográfica
        _finca: Plantación asociada
    """
    
    def __init__(
        self,
        padron: int,
        superficie: float,
        domicilio: str,
        finca: 'Plantacion'
    ):
        """
        Inicializa una Tierra.
        
        Args:
            padron: Número de padrón catastral
            superficie: Superficie en m2
            domicilio: Dirección de ubicación
            finca: Plantación asociada
        """
        self._padron = padron
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = finca
    
    def get_padron(self) -> int:
        """Retorna número de padrón."""
        return self._padron
    
    def set_padron(self, padron: int) -> None:
        """Establece número de padrón."""
        self._padron = padron
    
    def get_superficie(self) -> float:
        """Retorna superficie."""
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """Establece superficie."""
        self._superficie = superficie
    
    def get_domicilio(self) -> str:
        """Retorna domicilio."""
        return self._domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        """Establece domicilio."""
        self._domicilio = domicilio
    
    def get_finca(self) -> 'Plantacion':
        """Retorna plantación asociada."""
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        """Establece plantación asociada."""
        self._finca = finca