"""
Entidad Pino - Árbol conífera.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO


class Pino(Arbol):
    """
    Representa un árbol de Pino.
    
    Attributes:
        _variedad: Variedad del pino (Parana, Elliott, Taeda)
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa un Pino.
        
        Args:
            variedad: Variedad del pino
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=0.5
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """Retorna variedad del pino."""
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """Establece variedad del pino."""
        self._variedad = variedad