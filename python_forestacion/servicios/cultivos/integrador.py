"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 8
"""

# ================================================================================
# ARCHIVO 1/8: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/__init__.py
# ================================================================================

"""
Servicios de gestión de cultivos.
"""

# ================================================================================
# ARCHIVO 2/8: arbol_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/8: cultivo_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ================================================================================

"""
Servicio base para cultivos.
"""

from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService:
    """
    Servicio base para operaciones sobre cultivos.
    
    Attributes:
        _estrategia: Estrategia de absorción de agua
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa servicio.
        
        Args:
            estrategia: Estrategia de absorción inyectada
        """
        self._estrategia = estrategia
    
    def absorver_agua(
        self,
        cultivo: 'Cultivo',
        fecha: date = None,
        temperatura: float = 20.0,
        humedad: float = 50.0
    ) -> int:
        """
        Calcula y aplica absorción de agua usando Strategy.
        
        Args:
            cultivo: Cultivo que absorbe
            fecha: Fecha actual (default: hoy)
            temperatura: Temperatura ambiente
            humedad: Humedad relativa
            
        Returns:
            Litros absorbidos
        """
        if fecha is None:
            fecha = date.today()
        
        cantidad = self._estrategia.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + cantidad)
        
        return cantidad
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos del cultivo.
        
        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Agua: {cultivo.get_agua()} L")
        print(f"Superficie: {cultivo.get_superficie()} m2")

# ================================================================================
# ARCHIVO 4/8: cultivo_service_registry.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ================================================================================

"""
Registry de servicios de cultivos (Singleton + Registry Pattern).
"""

from threading import Lock
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry de servicios con patrón Singleton.
    Elimina instanceof mediante dispatch polimórfico.
    
    Thread-safe con double-checked locking.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        """
        Implementa Singleton thread-safe.
        
        Returns:
            Instancia única del registry
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar()
        return cls._instance
    
    def _inicializar(self):
        """Inicialización perezosa de servicios."""
        # Servicios específicos
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()
        
        # Registry de handlers por tipo
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        
        self._handlers_absorcion = {
            Pino: self._absorber_pino,
            Olivo: self._absorber_olivo,
            Lechuga: self._absorber_lechuga,
            Zanahoria: self._absorber_zanahoria
        }
        
        self._handlers_mostrar = {
            Pino: self._mostrar_pino,
            Olivo: self._mostrar_olivo,
            Lechuga: self._mostrar_lechuga,
            Zanahoria: self._mostrar_zanahoria
        }
        
        self._handlers_crecer = {
            Pino: self._crecer_pino,
            Olivo: self._crecer_olivo
        }
    
    @classmethod
    def get_instance(cls):
        """
        Retorna instancia única del registry.
        
        Returns:
            Instancia única
        """
        return cls()
    
    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Dispatch polimórfico para absorción.
        
        Args:
            cultivo: Cultivo que absorbe
            
        Returns:
            Litros absorbidos
            
        Raises:
            ValueError: Si tipo no registrado
        """
        tipo = type(cultivo)
        handler = self._handlers_absorcion.get(tipo)
        
        if handler is None:
            raise ValueError(f"Tipo no registrado: {tipo}")
        
        return handler(cultivo)
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Dispatch polimórfico para mostrar datos.
        
        Args:
            cultivo: Cultivo a mostrar
            
        Raises:
            ValueError: Si tipo no registrado
        """
        tipo = type(cultivo)
        handler = self._handlers_mostrar.get(tipo)
        
        if handler is None:
            raise ValueError(f"Tipo no registrado: {tipo}")
        
        handler(cultivo)
    
    def crecer(self, cultivo: 'Cultivo') -> None:
        """
        Dispatch polimórfico para crecimiento (solo árboles).
        
        Args:
            cultivo: Cultivo a hacer crecer
        """
        tipo = type(cultivo)
        handler = self._handlers_crecer.get(tipo)
        
        if handler is not None:
            handler(cultivo)
    
    # Handlers privados
    def _absorber_pino(self, pino: 'Pino') -> int:
        return self._pino_service.absorver_agua(pino)
    
    def _absorber_olivo(self, olivo: 'Olivo') -> int:
        return self._olivo_service.absorver_agua(olivo)
    
    def _absorber_lechuga(self, lechuga: 'Lechuga') -> int:
        return self._lechuga_service.absorver_agua(lechuga)
    
    def _absorber_zanahoria(self, zanahoria: 'Zanahoria') -> int:
        return self._zanahoria_service.absorver_agua(zanahoria)
    
    def _mostrar_pino(self, pino: 'Pino') -> None:
        self._pino_service.mostrar_datos(pino)
    
    def _mostrar_olivo(self, olivo: 'Olivo') -> None:
        self._olivo_service.mostrar_datos(olivo)
    
    def _mostrar_lechuga(self, lechuga: 'Lechuga') -> None:
        self._lechuga_service.mostrar_datos(lechuga)
    
    def _mostrar_zanahoria(self, zanahoria: 'Zanahoria') -> None:
        self._zanahoria_service.mostrar_datos(zanahoria)
    
    def _crecer_pino(self, pino: 'Pino') -> None:
        self._pino_service.crecer(pino)
    
    def _crecer_olivo(self, olivo: 'Olivo') -> None:
        self._olivo_service.crecer(olivo)

# ================================================================================
# ARCHIVO 5/8: lechuga_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 6/8: olivo_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 7/8: pino_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/pino_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 8/8: zanahoria_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ================================================================================

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

