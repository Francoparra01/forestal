"""
Paquete genérico tipo-seguro para empaquetado.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Contenedor genérico tipo-seguro.
    
    Type Parameters:
        T: Tipo de elementos contenidos
    """
    
    def __init__(self):
        """Inicializa paquete vacío."""
        self._items: List[T] = []
    
    def agregar(self, item: T) -> None:
        """
        Agrega un item al paquete.
        
        Args:
            item: Item a agregar
        """
        self._items.append(item)
    
    def obtener_todos(self) -> List[T]:
        """
        Retorna todos los items (copia defensiva).
        
        Returns:
            Lista de items
        """
        return self._items.copy()
    
    def cantidad(self) -> int:
        """
        Retorna cantidad de items.
        
        Returns:
            Número de items
        """
        return len(self._items)