"""
Servicio para gestión de plantaciones.
"""

from typing import TYPE_CHECKING

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """
    Servicio para operaciones sobre plantaciones.
    """
    
    def __init__(self):
        """Inicializa con registry de servicios."""
        self._registry = CultivoServiceRegistry.get_instance()
    
    def plantar(
        self,
        plantacion: 'Plantacion',
        especie: str,
        cantidad: int
    ) -> None:
        """
        Planta cultivos usando Factory Method.
        
        Args:
            plantacion: Plantación donde plantar
            especie: Especie a plantar
            cantidad: Cantidad a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay superficie
        """
        # Crear uno para calcular superficie requerida
        cultivo_muestra = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )
        
        # Plantar
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)
        
        # Actualizar superficie
        nueva_superficie = superficie_disponible - superficie_requerida
        plantacion.set_superficie_disponible(nueva_superficie)
    
    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantación.
        
        Args:
            plantacion: Plantación a regar
            
        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        cultivos = plantacion.get_cultivos()
        agua_disponible = plantacion.get_agua_disponible()
        
        # Calcular agua total necesaria
        agua_necesaria = 0
        for cultivo in cultivos:
            agua_necesaria += 5  # Estimación conservadora
        
        if agua_necesaria > agua_disponible:
            raise AguaAgotadaException(agua_necesaria, agua_disponible)
        
        # Regar cada cultivo
        for cultivo in cultivos:
            cantidad = self._registry.absorber_agua(cultivo)
            agua_disponible -= cantidad
            
            # Hacer crecer si es árbol
            self._registry.crecer(cultivo)
        
        plantacion.set_agua_disponible(agua_disponible)
    
    def cosechar(self, plantacion: 'Plantacion') -> None:
        """
        Cosecha los cultivos de la plantación.
        
        Args:
            plantacion: Plantación a cosechar
        """
        cultivos = plantacion.get_cultivos()
        print(f"[INFO] Cosechando {len(cultivos)} cultivos...")
    
    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """
        Aplica fumigación a la plantación.
        
        Args:
            plantacion: Plantación a fumigar
            plaguicida: Tipo de plaguicida
        """
        print(f"[INFO] Aplicando {plaguicida} a plantacion...")