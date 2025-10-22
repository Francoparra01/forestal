"""
Controlador de riego (Observer).
"""

import threading
import time
from typing import TYPE_CHECKING

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Thread que controla riego automático basado en sensores.
    Implementa patrón Observer como Observer.
    """
    
    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa controlador de riego.
        
        Args:
            sensor_temperatura: Sensor de temperatura a observar
            sensor_humedad: Sensor de humedad a observar
            plantacion: Plantación a regar
            plantacion_service: Servicio de plantación
        """
        threading.Thread.__init__(self, daemon=True)
        
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        
        self._ultima_temperatura = 20.0
        self._ultima_humedad = 50.0
        
        self._detenido = threading.Event()
        
        # Suscribirse a sensores (Observer pattern)
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)
    
    def actualizar(self, evento: float) -> None:
        """
        Método del Observer - recibe notificaciones de sensores.
        
        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        # Determinar si es temperatura o humedad por rango
        if -25 <= evento <= 50:  # Rango de temperatura
            self._ultima_temperatura = evento
        else:  # Rango de humedad
            self._ultima_humedad = evento
    
    def run(self):
        """
        Bucle principal del controlador.
        Evalúa condiciones cada INTERVALO_CONTROL_RIEGO segundos.
        """
        while not self._detenido.is_set():
            self._evaluar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)
    
    def _evaluar_y_regar(self):
        """
        Evalúa condiciones y riega si se cumplen.
        
        Condiciones para riego:
        - TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO
        - humedad < HUMEDAD_MAX_RIEGO
        """
        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO
        
        if temp_ok and humedad_ok:
            try:
                self._plantacion_service.regar(self._plantacion)
                print(f"[RIEGO] T={self._ultima_temperatura:.1f}C, "
                      f"H={self._ultima_humedad:.1f}% -> RIEGO ACTIVADO")
            except Exception as e:
                print(f"[ERROR] Fallo en riego: {e}")
    
    def detener(self):
        """Detiene el thread de forma controlada."""
        self._detenido.set()