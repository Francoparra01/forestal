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