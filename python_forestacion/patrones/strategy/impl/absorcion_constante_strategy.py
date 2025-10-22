"""
Estrategia de absorción constante.
"""

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia con absorción constante independiente de la estación.
    Usada para hortalizas (Lechuga, Zanahoria).
    """

    def __init__(self, cantidad_constante: float = 0.4):
        """
        Inicializa la estrategia.

        Args:
            cantidad_constante: Litros constantes a absorber.
        """
        self._cantidad = float(cantidad_constante)

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: "Cultivo",
    ) -> float:
        """
        Retorna una cantidad constante de agua absorbida.

        Args:
            fecha: No usado en esta estrategia.
            temperatura: No usado.
            humedad: No usado.
            cultivo: Cultivo que absorbe.

        Returns:
            Litros constantes de agua absorbidos.
        """
        return self._cantidad

