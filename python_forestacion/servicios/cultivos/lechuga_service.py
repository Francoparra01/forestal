"""
Servicio para Lechuga.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio específico para Lechuga.
    Usa estrategia constante.
    """
    
    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))
    
    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos específicos de la lechuga.
        
        Args:
            lechuga: Lechuga a mostrar
        """
        super().mostrar_datos(lechuga)
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")