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