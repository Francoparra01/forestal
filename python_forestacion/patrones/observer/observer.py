"""
Interfaz Observer para patrón Observer.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(ABC, Generic[T]):
    """
    Interfaz para observadores tipo-seguros.
    
    Type Parameters:
        T: Tipo del evento que observa
    """
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el observable notifica un cambio.
        
        Args:
            evento: Dato del evento
        """
        pass