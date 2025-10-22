"""
Interfaz Strategy para absorción de agua.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz para estrategias de absorción de agua.
    Implementa patrón Strategy.
    """
    
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula cantidad de agua a absorber.
        
        Args:
            fecha: Fecha actual
            temperatura: Temperatura ambiente en °C
            humedad: Humedad relativa en %
            cultivo: Cultivo que absorbe
            
        Returns:
            Cantidad de agua en litros
        """
        pass