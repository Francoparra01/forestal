"""
Entidad Zanahoria - Hortaliza de raíz.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA


class Zanahoria(Hortaliza):
    """
    Representa una zanahoria.
    
    Attributes:
        _es_baby: Indica si es baby carrot
    """
    
    def __init__(self, es_baby: bool = False):
        """
        Inicializa una Zanahoria.
        
        Args:
            es_baby: True si es baby carrot
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby
    
    def get_es_baby(self) -> bool:
        """Retorna si es baby carrot."""
        return self._es_baby
    
    def set_es_baby(self, es_baby: bool) -> None:
        """Establece si es baby carrot."""
        self._es_baby = es_baby