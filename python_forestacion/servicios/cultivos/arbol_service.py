"""
Servicio base para árboles.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """
    Servicio base para árboles.
    Extiende CultivoService con operaciones específicas de árboles.
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa servicio de árbol.
        
        Args:
            estrategia: Estrategia de absorción
        """
        super().__init__(estrategia)
    
    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del árbol incluyendo altura.
        
        Args:
            arbol: Árbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"Altura: {arbol.get_altura():.2f} m")