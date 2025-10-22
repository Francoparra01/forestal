"""
Entidad AptoMedico - Certificación médica.
"""

from datetime import date


class AptoMedico:
    """
    Representa una certificación médica para trabajo agrícola.
    
    Attributes:
        _fecha_emision: Fecha de emisión del apto
        _observaciones: Observaciones médicas
    """
    
    def __init__(self, fecha_emision: date, observaciones: str):
        """
        Inicializa un AptoMedico.
        
        Args:
            fecha_emision: Fecha de emisión
            observaciones: Observaciones médicas
        """
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones
    
    def get_fecha_emision(self) -> date:
        """Retorna fecha de emisión."""
        return self._fecha_emision
    
    def set_fecha_emision(self, fecha: date) -> None:
        """Establece fecha de emisión."""
        self._fecha_emision = fecha
    
    def get_observaciones(self) -> str:
        """Retorna observaciones."""
        return self._observaciones
    
    def set_observaciones(self, observaciones: str) -> None:
        """Establece observaciones."""
        self._observaciones = observaciones
    
    def es_valido(self) -> bool:
        """
        Verifica si el apto médico es válido.
        
        Returns:
            True si fue emitido, False si no tiene fecha
        """
        return self._fecha_emision is not None