"""
Entidad RegistroForestal - Registro legal completo.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Representa un registro forestal legal completo.
    
    Attributes:
        _id_padron: Identificador de padrón
        _tierra: Parcela catastral
        _plantacion: Plantación asociada
        _propietario: Nombre del propietario
        _avaluo: Avalúo fiscal
    """
    
    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un RegistroForestal.
        
        Args:
            id_padron: Identificador de padrón
            tierra: Tierra asociada
            plantacion: Plantación asociada
            propietario: Nombre del propietario
            avaluo: Avalúo fiscal en pesos
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        """Retorna ID de padrón."""
        return self._id_padron
    
    def set_id_padron(self, id_padron: int) -> None:
        """Establece ID de padrón."""
        self._id_padron = id_padron
    
    def get_tierra(self) -> 'Tierra':
        """Retorna tierra asociada."""
        return self._tierra
    
    def set_tierra(self, tierra: 'Tierra') -> None:
        """Establece tierra asociada."""
        self._tierra = tierra
    
    def get_plantacion(self) -> 'Plantacion':
        """Retorna plantación asociada."""
        return self._plantacion
    
    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """Establece plantación asociada."""
        self._plantacion = plantacion
    
    def get_propietario(self) -> str:
        """Retorna nombre del propietario."""
        return self._propietario
    
    def set_propietario(self, propietario: str) -> None:
        """Establece nombre del propietario."""
        self._propietario = propietario
    
    def get_avaluo(self) -> float:
        """Retorna avalúo fiscal."""
        return self._avaluo
    
    def set_avaluo(self, avaluo: float) -> None:
        """Establece avalúo fiscal."""
        self._avaluo = avaluo