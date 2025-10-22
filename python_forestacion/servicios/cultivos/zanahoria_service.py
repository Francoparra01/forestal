"""
Servicio para Zanahoria.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio específico para Zanahoria.
    Usa estrategia constante.
    """
    
    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))
    
    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos específicos de la zanahoria.
        
        Args:
            zanahoria: Zanahoria a mostrar
        """
        super().mostrar_datos(zanahoria)
        print(f"Baby carrot: {zanahoria.get_es_baby()}")
        print(f"Invernadero: {zanahoria.get_invernadero()}")