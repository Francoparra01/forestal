"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: registro_forestal_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ================================================================================

"""
Servicio para persistencia de registros forestales.
"""

import os
import pickle
from typing import TYPE_CHECKING

from python_forestacion.excepciones.persistencia_exception import PersistenciaException
from python_forestacion.constantes import DIRECTORIO_DATA, EXTENSION_ARCHIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal


class RegistroForestalService:
    """
    Servicio para persistencia de registros forestales.
    """
    
    def persistir(self, registro: 'RegistroForestal') -> None:
        """
        Persiste registro en disco usando Pickle.
        
        Args:
            registro: Registro a persistir
            
        Raises:
            PersistenciaException: Si falla persistencia
        """
        try:
            # Crear directorio si no existe
            if not os.path.exists(DIRECTORIO_DATA):
                os.makedirs(DIRECTORIO_DATA)
            
            # Nombre archivo
            nombre_archivo = f"{registro.get_propietario()}{EXTENSION_ARCHIVO}"
            ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
            
            # Serializar
            with open(ruta_completa, 'wb') as archivo:
                pickle.dump(registro, archivo)
        
        except Exception as e:
            raise PersistenciaException(f"Error al guardar: {str(e)}")
    
    @staticmethod
    def leer_registro(propietario: str) -> 'RegistroForestal':
        """
        Lee registro desde disco.
        
        Args:
            propietario: Nombre del propietario
            
        Returns:
            Registro recuperado
            
        Raises:
            PersistenciaException: Si falla lectura
        """
        try:
            nombre_archivo = f"{propietario}{EXTENSION_ARCHIVO}"
            ruta_completa = os.path.join(DIRECTORIO_DATA, nombre_archivo)
            
            with open(ruta_completa, 'rb') as archivo:
                registro = pickle.load(archivo)
            
            return registro
        
        except FileNotFoundError:
            raise PersistenciaException(f"Archivo no encontrado: {propietario}")
        except Exception as e:
            raise PersistenciaException(f"Error al leer: {str(e)}")
    
    def mostrar_datos(self, registro: 'RegistroForestal') -> None:
        """
        Muestra datos del registro.
        
        Args:
            registro: Registro a mostrar
        """
        print(f"Propietario: {registro.get_propietario()}")
        print(f"Padron: {registro.get_id_padron()}")
        print(f"Avaluo: ${registro.get_avaluo():,.2f}")
        print(f"Plantacion: {registro.get_plantacion().get_nombre()}")
        print(f"Cultivos: {len(registro.get_plantacion().get_cultivos())}")

# ================================================================================
# ARCHIVO 4/4: tierra_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/tierra_service.py
# ================================================================================

"""
Servicio para gestión de tierras.
"""

from python_forestacion.entidades.terrenos.tierra import Tierra
from python_forestacion.entidades.terrenos.plantacion import Plantacion


class TierraService:
    """
    Servicio para operaciones sobre tierras.
    """
    
    def crear_tierra_con_plantacion(
        self,
        id_padron_catastral: int,
        superficie: float,
        domicilio: str,
        nombre_plantacion: str
    ) -> Tierra:
        """
        Crea una tierra con plantación asociada.
        
        Args:
            id_padron_catastral: Padrón catastral
            superficie: Superficie en m2
            domicilio: Dirección
            nombre_plantacion: Nombre de la plantación
            
        Returns:
            Tierra creada con plantación
        """
        plantacion = Plantacion(nombre_plantacion, superficie)
        
        tierra = Tierra(
            padron=id_padron_catastral,
            superficie=superficie,
            domicilio=domicilio,
            finca=plantacion
        )
        
        return tierra
    
    def mostrar_datos(self, tierra: Tierra) -> None:
        """
        Muestra datos de la tierra.
        
        Args:
            tierra: Tierra a mostrar
        """
        print(f"Padron: {tierra.get_padron()}")
        print(f"Superficie: {tierra.get_superficie()} m2")
        print(f"Domicilio: {tierra.get_domicilio()}")
        print(f"Plantacion: {tierra.get_finca().get_nombre()}")

