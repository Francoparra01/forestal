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