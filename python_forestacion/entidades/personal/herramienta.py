"""
Entidad Herramienta - Equipamiento de trabajo.
"""


class Herramienta:
    """
    Representa una herramienta de trabajo.
    
    Attributes:
        _id: Identificador único
        _nombre: Nombre de la herramienta
        _certificacion_hs: Certificación de higiene y seguridad
    """
    
    def __init__(self, id_herramienta: int, nombre: str, certificacion_hs: str):
        """
        Inicializa una Herramienta.
        
        Args:
            id_herramienta: ID único
            nombre: Nombre descriptivo
            certificacion_hs: Certificación H&S
        """
        self._id = id_herramienta
        self._nombre = nombre
        self._certificacion_hs = certificacion_hs
    
    def get_id(self) -> int:
        """Retorna ID de la herramienta."""
        return self._id
    
    def set_id(self, id_herramienta: int) -> None:
        """Establece ID de la herramienta."""
        self._id = id_herramienta
    
    def get_nombre(self) -> str:
        """Retorna nombre de la herramienta."""
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """Establece nombre de la herramienta."""
        self._nombre = nombre
    
    def get_certificacion_hs(self) -> str:
        """Retorna certificación H&S."""
        return self._certificacion_hs
    
    def set_certificacion_hs(self, certificacion: str) -> None:
        """Establece certificación H&S."""
        self._certificacion_hs = certificacion