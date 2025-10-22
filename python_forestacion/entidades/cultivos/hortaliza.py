"""
Clase base para cultivos hortícolas.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """
    Clase base para hortalizas.
    
    Attributes:
        _invernadero: Indica si requiere invernadero
    """
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie que ocupa en m2
            invernadero: True si requiere invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero
    
    def get_invernadero(self) -> bool:
        """Retorna si requiere invernadero."""
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        """Establece requerimiento de invernadero."""
        self._invernadero = invernadero