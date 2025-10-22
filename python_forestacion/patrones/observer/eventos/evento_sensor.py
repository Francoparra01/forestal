"""
Evento de sensores ambientales.
"""


class EventoSensor:
    """
    Representa un evento de lectura de sensor.
    
    Attributes:
        _tipo: Tipo de sensor ("temperatura" o "humedad")
        _valor: Valor leído
    """
    
    def __init__(self, tipo: str, valor: float):
        """
        Inicializa un EventoSensor.
        
        Args:
            tipo: Tipo de sensor
            valor: Valor leído
        """
        self._tipo = tipo
        self._valor = valor
    
    def get_tipo(self) -> str:
        """Retorna tipo de sensor."""
        return self._tipo
    
    def get_valor(self) -> float:
        """Retorna valor leído."""
        return self._valor