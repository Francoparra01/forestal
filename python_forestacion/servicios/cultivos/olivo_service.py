"""
Servicio para Olivo.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio específico para Olivo.
    Usa estrategia seasonal.
    """
    
    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """
        Hace crecer el olivo.
        
        Args:
            olivo: Olivo a hacer crecer
        """
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO)
    
    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos específicos del olivo.
        
        Args:
            olivo: Olivo a mostrar
        """
        super().mostrar_datos(olivo)
        print(f"Tipo aceituna: {olivo.get_tipo_aceituna().value}")