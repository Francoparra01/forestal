"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/riego/sensores
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/riego/sensores/__init__.py
# ================================================================================

"""
Sensores ambientales.
"""

# ================================================================================
# ARCHIVO 2/3: humedad_reader_task.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ================================================================================

"""
Sensor de humedad (Observable).
"""

import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    HUMEDAD_MIN_SENSOR,
    HUMEDAD_MAX_SENSOR
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee humedad y notifica a observadores.
    Implementa patrón Observer como Observable.
    """
    
    def __init__(self):
        """Inicializa sensor de humedad."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self):
        """
        Bucle principal del sensor.
        Lee humedad cada INTERVALO_SENSOR_HUMEDAD segundos.
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)
    
    def _leer_humedad(self) -> float:
        """
        Simula lectura de sensor de humedad.
        
        Returns:
            Humedad relativa en %
        """
        return random.uniform(HUMEDAD_MIN_SENSOR, HUMEDAD_MAX_SENSOR)
    
    def detener(self):
        """Detiene el thread de forma controlada."""
        self._detenido.set()

# ================================================================================
# ARCHIVO 3/3: temperatura_reader_task.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ================================================================================

"""
Sensor de temperatura (Observable).
"""

import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_MIN_SENSOR,
    TEMP_MAX_SENSOR
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee temperatura y notifica a observadores.
    Implementa patrón Observer como Observable.
    """
    
    def __init__(self):
        """Inicializa sensor de temperatura."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self):
        """
        Bucle principal del sensor.
        Lee temperatura cada INTERVALO_SENSOR_TEMPERATURA segundos.
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
    
    def _leer_temperatura(self) -> float:
        """
        Simula lectura de sensor de temperatura.
        
        Returns:
            Temperatura en °C
        """
        return random.uniform(TEMP_MIN_SENSOR, TEMP_MAX_SENSOR)
    
    def detener(self):
        """Detiene el thread de forma controlada."""
        self._detenido.set()

