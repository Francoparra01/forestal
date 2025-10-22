"""
Servicio para Pino.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio específico para Pino.
    Usa estrategia seasonal.
    """
    
    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """
        Hace crecer el pino.
        
        Args:
            pino: Pino a hacer crecer
        """
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO)
    
    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos específicos del pino.
        
        Args:
            pino: Pino a mostrar
        """
        super().mostrar_datos(pino)
        print(f"Variedad: {pino.get_variedad()}")