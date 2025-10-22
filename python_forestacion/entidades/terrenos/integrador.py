"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: plantacion.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/plantacion.py
# ================================================================================

"""
Entidad Plantación - Agrupación de cultivos.
"""

from typing import List, TYPE_CHECKING

from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Representa una plantación agrícola.
    
    Attributes:
        _nombre: Nombre identificatorio
        _superficie_disponible: Superficie libre en m2
        _cultivos: Lista de cultivos plantados
        _agua_disponible: Agua disponible en litros
        _trabajadores: Personal asignado
    """
    
    def __init__(self, nombre: str, superficie_total: float):
        """
        Inicializa una Plantación.
        
        Args:
            nombre: Nombre de la plantación
            superficie_total: Superficie total en m2
        """
        self._nombre = nombre
        self._superficie_disponible = superficie_total
        self._cultivos: List['Cultivo'] = []
        self._agua_disponible = AGUA_INICIAL_PLANTACION
        self._trabajadores: List['Trabajador'] = []
    
    def get_nombre(self) -> str:
        """Retorna nombre de la plantación."""
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """Establece nombre de la plantación."""
        self._nombre = nombre
    
    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible
    
    def set_superficie_disponible(self, superficie: float) -> None:
        """Establece superficie disponible."""
        self._superficie_disponible = superficie
    
    def get_cultivos(self) -> List['Cultivo']:
        """Retorna lista de cultivos (copia defensiva)."""
        return self._cultivos.copy()
    
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo a la plantación."""
        self._cultivos.append(cultivo)
    
    def get_agua_disponible(self) -> int:
        """Retorna agua disponible."""
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        """Establece agua disponible."""
        self._agua_disponible = agua
    
    def get_trabajadores(self) -> List['Trabajador']:
        """Retorna lista de trabajadores (copia defensiva)."""
        return self._trabajadores.copy()
    
    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        """Agrega un trabajador a la plantación."""
        self._trabajadores.append(trabajador)

# ================================================================================
# ARCHIVO 3/4: registro_forestal.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ================================================================================

"""
Entidad RegistroForestal - Registro legal completo.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Representa un registro forestal legal completo.
    
    Attributes:
        _id_padron: Identificador de padrón
        _tierra: Parcela catastral
        _plantacion: Plantación asociada
        _propietario: Nombre del propietario
        _avaluo: Avalúo fiscal
    """
    
    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un RegistroForestal.
        
        Args:
            id_padron: Identificador de padrón
            tierra: Tierra asociada
            plantacion: Plantación asociada
            propietario: Nombre del propietario
            avaluo: Avalúo fiscal en pesos
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        """Retorna ID de padrón."""
        return self._id_padron
    
    def set_id_padron(self, id_padron: int) -> None:
        """Establece ID de padrón."""
        self._id_padron = id_padron
    
    def get_tierra(self) -> 'Tierra':
        """Retorna tierra asociada."""
        return self._tierra
    
    def set_tierra(self, tierra: 'Tierra') -> None:
        """Establece tierra asociada."""
        self._tierra = tierra
    
    def get_plantacion(self) -> 'Plantacion':
        """Retorna plantación asociada."""
        return self._plantacion
    
    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """Establece plantación asociada."""
        self._plantacion = plantacion
    
    def get_propietario(self) -> str:
        """Retorna nombre del propietario."""
        return self._propietario
    
    def set_propietario(self, propietario: str) -> None:
        """Establece nombre del propietario."""
        self._propietario = propietario
    
    def get_avaluo(self) -> float:
        """Retorna avalúo fiscal."""
        return self._avaluo
    
    def set_avaluo(self, avaluo: float) -> None:
        """Establece avalúo fiscal."""
        self._avaluo = avaluo

# ================================================================================
# ARCHIVO 4/4: tierra.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/tierra.py
# ================================================================================

"""
Entidad Tierra - Parcela catastral.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Representa una parcela de tierra catastral.
    
    Attributes:
        _padron: Número de padrón catastral único
        _superficie: Superficie en metros cuadrados
        _domicilio: Ubicación geográfica
        _finca: Plantación asociada
    """
    
    def __init__(
        self,
        padron: int,
        superficie: float,
        domicilio: str,
        finca: 'Plantacion'
    ):
        """
        Inicializa una Tierra.
        
        Args:
            padron: Número de padrón catastral
            superficie: Superficie en m2
            domicilio: Dirección de ubicación
            finca: Plantación asociada
        """
        self._padron = padron
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = finca
    
    def get_padron(self) -> int:
        """Retorna número de padrón."""
        return self._padron
    
    def set_padron(self, padron: int) -> None:
        """Establece número de padrón."""
        self._padron = padron
    
    def get_superficie(self) -> float:
        """Retorna superficie."""
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """Establece superficie."""
        self._superficie = superficie
    
    def get_domicilio(self) -> str:
        """Retorna domicilio."""
        return self._domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        """Establece domicilio."""
        self._domicilio = domicilio
    
    def get_finca(self) -> 'Plantacion':
        """Retorna plantación asociada."""
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        """Establece plantación asociada."""
        self._finca = finca

