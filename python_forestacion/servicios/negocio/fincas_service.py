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