"""
Entidad Olivo - Árbol frutal.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO


class Olivo(Arbol):
    """
    Representa un árbol de Olivo.
    
    Attributes:
        _tipo_aceituna: Tipo de aceituna que produce
    """
    
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un Olivo.
        
        Args:
            tipo_aceituna: Tipo de aceituna
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=1.0
        )
        self._tipo_aceituna = tipo_aceituna
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        """Retorna tipo de aceituna."""
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """Establece tipo de aceituna."""
        self._tipo_aceituna = tipo_aceituna