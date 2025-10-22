"""
Entidad Plantación - Agrupación de cultivos.
"""

from typing import List, TYPE_CHECKING

from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Representa una plantación agrícola.
    
    Attributes:
        _nombre: Nombre identificatorio
        _superficie_disponible: Superficie libre en m2
        _cultivos: Lista de cultivos plantados
        _agua_disponible: Agua disponible en litros
        _trabajadores: Personal asignado
    """
    
    def __init__(self, nombre: str, superficie_total: float):
        """
        Inicializa una Plantación.
        
        Args:
            nombre: Nombre de la plantación
            superficie_total: Superficie total en m2
        """
        self._nombre = nombre
        self._superficie_disponible = superficie_total
        self._cultivos: List['Cultivo'] = []
        self._agua_disponible = AGUA_INICIAL_PLANTACION
        self._trabajadores: List['Trabajador'] = []
    
    def get_nombre(self) -> str:
        """Retorna nombre de la plantación."""
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """Establece nombre de la plantación."""
        self._nombre = nombre
    
    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible
    
    def set_superficie_disponible(self, superficie: float) -> None:
        """Establece superficie disponible."""
        self._superficie_disponible = superficie
    
    def get_cultivos(self) -> List['Cultivo']:
        """Retorna lista de cultivos (copia defensiva)."""
        return self._cultivos.copy()
    
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo a la plantación."""
        self._cultivos.append(cultivo)
    
    def get_agua_disponible(self) -> int:
        """Retorna agua disponible."""
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        """Establece agua disponible."""
        self._agua_disponible = agua
    
    def get_trabajadores(self) -> List['Trabajador']:
        """Retorna lista de trabajadores (copia defensiva)."""
        return self._trabajadores.copy()
    
    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        """Agrega un trabajador a la plantación."""
        self._trabajadores.append(trabajador)