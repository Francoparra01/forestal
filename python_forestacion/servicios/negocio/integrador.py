"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio/__init__.py
# ================================================================================

"""
Servicios de alto nivel de negocio.
"""

# ================================================================================
# ARCHIVO 2/3: fincas_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio/fincas_service.py
# ================================================================================

"""
Servicio de alto nivel para operaciones en fincas.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal


class FincasService:
    """
    Servicio de alto nivel para gestión integral de fincas.
    """
    
    def generar_reporte(self, registro: 'RegistroForestal') -> str:
        """
        Genera reporte completo de la finca.
        
        Args:
            registro: Registro forestal
            
        Returns:
            Reporte en formato texto
        """
        plantacion = registro.get_plantacion()
        tierra = registro.get_tierra()
        
        reporte = []
        reporte.append("=" * 60)
        reporte.append("REPORTE DE FINCA")
        reporte.append("=" * 60)
        reporte.append(f"Propietario: {registro.get_propietario()}")
        reporte.append(f"Padron: {registro.get_id_padron()}")
        reporte.append(f"Domicilio: {tierra.get_domicilio()}")
        reporte.append(f"Superficie total: {tierra.get_superficie()} m2")
        reporte.append(f"Avaluo: ${registro.get_avaluo():,.2f}")
        reporte.append("")
        reporte.append(f"Plantacion: {plantacion.get_nombre()}")
        reporte.append(f"Cultivos: {len(plantacion.get_cultivos())}")
        reporte.append(f"Trabajadores: {len(plantacion.get_trabajadores())}")
        reporte.append(f"Agua disponible: {plantacion.get_agua_disponible()} L")
        reporte.append("=" * 60)
        
        return "\n".join(reporte)

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio/paquete.py
# ================================================================================

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

