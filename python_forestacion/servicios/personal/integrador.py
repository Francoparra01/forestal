"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/servicios/personal
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/personal/__init__.py
# ================================================================================

"""
Servicios de gestión de personal.
"""

# ================================================================================
# ARCHIVO 2/2: trabajador_service.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/servicios/personal/trabajador_service.py
# ================================================================================

"""
Servicio para gestión de trabajadores.
"""

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.trabajador import Trabajador
    from python_forestacion.entidades.personal.herramienta import Herramienta


class TrabajadorService:
    """
    Servicio para operaciones sobre trabajadores.
    """
    
    def trabajar(
        self,
        trabajador: 'Trabajador',
        fecha: date,
        herramienta: 'Herramienta'
    ) -> bool:
        """
        Ejecuta tareas del trabajador si tiene apto médico.
        
        Args:
            trabajador: Trabajador que ejecuta
            fecha: Fecha de ejecución
            herramienta: Herramienta a usar
            
        Returns:
            True si ejecutó tareas, False si no tiene apto
        """
        # Verificar apto médico
        apto = trabajador.get_apto_medico()
        if apto is None or not apto.es_valido():
            print(f"[ERROR] Trabajador {trabajador.get_nombre()} sin apto medico")
            return False
        
        # Ejecutar tareas pendientes
        tareas = trabajador.get_tareas()
        tareas_ejecutadas = 0
        
        for tarea in tareas:
            if not tarea.esta_completada() and tarea.get_fecha_programada() <= fecha:
                tarea.marcar_completada()
                tareas_ejecutadas += 1
        
        if tareas_ejecutadas > 0:
            print(f"[OK] {tareas_ejecutadas} tarea(s) ejecutada(s) con {herramienta.get_nombre()}")
        
        return True

