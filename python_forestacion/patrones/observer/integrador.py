"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/patrones/observer
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/__init__.py
# ================================================================================

"""
Patrón Observer.
"""

# ================================================================================
# ARCHIVO 2/3: observable.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/observable.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/3: observer.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/observer.py
# ================================================================================

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

