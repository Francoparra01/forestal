"""
Estrategia de absorción estacional.
"""

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua que varía según la temperatura y la humedad.
    Usada para árboles (Pino, Olivo).
    """

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: "Cultivo",
    ) -> float:
        """
        Calcula la cantidad de agua absorbida según estación simulada.
        A mayor temperatura y menor humedad, más absorción.

        Args:
            fecha: Fecha actual (se puede usar para estacionalidad)
            temperatura: Temperatura ambiente en °C
            humedad: Humedad relativa (0–1)
            cultivo: Cultivo que absorbe

        Returns:
            Litros de agua absorbidos.
        """
        base = 0.5  # L/h de referencia
        factor_temp = max(0.0, (temperatura - 10.0)) * 0.03
        factor_humedad = max(0.0, 1.0 - min(1.0, humedad))
        return base * (1.0 + factor_temp) * (1.0 + 0.5 * factor_humedad)

        return self._cantidad
