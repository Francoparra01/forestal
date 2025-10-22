"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos/__init__.py
# ================================================================================

"""
Eventos del sistema.
"""

# ================================================================================
# ARCHIVO 2/3: evento_plantacion.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ================================================================================

"""
Evento de operaciones en plantación.
"""


class EventoPlantacion:
    """
    Representa un evento operativo en plantación.
    
    Attributes:
        _tipo: Tipo de evento ("riego", "cosecha", "fumigacion")
        _descripcion: Descripción del evento
    """
    
    def __init__(self, tipo: str, descripcion: str):
        """
        Inicializa un EventoPlantacion.
        
        Args:
            tipo: Tipo de evento
            descripcion: Descripción detallada
        """
        self._tipo = tipo
        self._descripcion = descripcion
    
    def get_tipo(self) -> str:
        """Retorna tipo de evento."""
        return self._tipo
    
    def get_descripcion(self) -> str:
        """Retorna descripción."""
        return self._descripcion

# ================================================================================
# ARCHIVO 3/3: evento_sensor.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ================================================================================

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

