"""
Excepción de errores de persistencia.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_PERSISTENCIA_ERROR_USER,
    MSG_PERSISTENCIA_ERROR_TECH
)


class PersistenciaException(ForestacionException):
    """
    Excepción lanzada en errores de persistencia.
    """
    
    def __init__(self, detalle: str):
        """
        Inicializa la excepción.
        
        Args:
            detalle: Detalle del error
        """
        user_msg = MSG_PERSISTENCIA_ERROR_USER
        tech_msg = f"{MSG_PERSISTENCIA_ERROR_TECH}: {detalle}"
        super().__init__(user_msg, tech_msg)