"""
Clase base para cultivos arbóreos.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo):
    """
    Clase base para árboles.
    
    Attributes:
        _altura: Altura del árbol en metros
    """
    
    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un árbol.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie que ocupa en m2
            altura: Altura inicial en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura
    
    def get_altura(self) -> float:
        """Retorna altura del árbol."""
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        """Establece altura del árbol."""
        self._altura = altura