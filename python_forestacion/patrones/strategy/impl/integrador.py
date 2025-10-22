"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ================================================================================

"""
Implementaciones concretas de estrategias.
"""

# ================================================================================
# ARCHIVO 2/3: absorcion_constante_strategy.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ================================================================================

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



# ================================================================================
# ARCHIVO 3/3: absorcion_seasonal_strategy.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ================================================================================

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


