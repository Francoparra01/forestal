"""
Clase base Observable para patrón Observer.
"""

from abc import ABC
from typing import Generic, TypeVar, List

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(ABC, Generic[T]):
    """
    Clase base para objetos observables tipo-seguros.
    
    Type Parameters:
        T: Tipo del evento que notifica
    """
    
    def __init__(self):
        """Inicializa lista de observadores."""
        self._observadores: List[Observer[T]] = []
    
    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador.
        
        Args:
            observador: Observador a agregar
        """
        self._observadores.append(observador)
    
    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador.
        
        Args:
            observador: Observador a eliminar
        """
        self._observadores.remove(observador)
    
    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores.
        
        Args:
            evento: Dato del evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)