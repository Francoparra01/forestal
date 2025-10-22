"""
Entidad Tarea - Labor asignada.
"""

from datetime import date


class Tarea:
    """
    Representa una tarea agrícola.
    
    Attributes:
        _id: Identificador único
        _descripcion: Descripción de la tarea
        _fecha_programada: Fecha programada
        _completada: Estado de completitud
    """
    
    def __init__(self, id_tarea: int, descripcion: str, fecha_programada: date):
        """
        Inicializa una Tarea.
        
        Args:
            id_tarea: ID único
            descripcion: Descripción de la labor
            fecha_programada: Fecha programada
        """
        self._id = id_tarea
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._completada = False
    
    def get_id(self) -> int:
        """Retorna ID de la tarea."""
        return self._id
    
    def set_id(self, id_tarea: int) -> None:
        """Establece ID de la tarea."""
        self._id = id_tarea
    
    def get_descripcion(self) -> str:
        """Retorna descripción."""
        return self._descripcion
    
    def set_descripcion(self, descripcion: str) -> None:
        """Establece descripción."""
        self._descripcion = descripcion
    
    def get_fecha_programada(self) -> date:
        """Retorna fecha programada."""
        return self._fecha_programada
    
    def set_fecha_programada(self, fecha: date) -> None:
        """Establece fecha programada."""
        self._fecha_programada = fecha
    
    def esta_completada(self) -> bool:
        """Retorna si está completada."""
        return self._completada
    
    def marcar_completada(self) -> None:
        """Marca la tarea como completada."""
        self._completada = True