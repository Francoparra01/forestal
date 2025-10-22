"""
Entidad Trabajador - Personal agrícola.
"""

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.personal.tarea import Tarea
    from python_forestacion.entidades.personal.apto_medico import AptoMedico


class Trabajador:
    """
    Representa un trabajador agrícola.
    
    Attributes:
        _dni: Documento Nacional de Identidad
        _nombre: Nombre completo
        _tareas: Lista de tareas asignadas
        _apto_medico: Certificación médica
    """
    
    def __init__(
        self,
        dni: int,
        nombre: str,
        tareas: List['Tarea'],
        apto_medico: Optional['AptoMedico'] = None
    ):
        """
        Inicializa un Trabajador.
        
        Args:
            dni: DNI del trabajador
            nombre: Nombre completo
            tareas: Lista de tareas asignadas
            apto_medico: Certificación médica (opcional)
        """
        self._dni = dni
        self._nombre = nombre
        self._tareas = tareas
        self._apto_medico = apto_medico
    
    def get_dni(self) -> int:
        """Retorna DNI."""
        return self._dni
    
    def set_dni(self, dni: int) -> None:
        """Establece DNI."""
        self._dni = dni
    
    def get_nombre(self) -> str:
        """Retorna nombre."""
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """Establece nombre."""
        self._nombre = nombre
    
    def get_tareas(self) -> List['Tarea']:
        """Retorna lista de tareas (copia defensiva)."""
        return self._tareas.copy()
    
    def agregar_tarea(self, tarea: 'Tarea') -> None:
        """Agrega una tarea."""
        self._tareas.append(tarea)
    
    def get_apto_medico(self) -> Optional['AptoMedico']:
        """Retorna apto médico."""
        return self._apto_medico
    
    def set_apto_medico(self, apto: 'AptoMedico') -> None:
        """Establece apto médico."""
        self._apto_medico = apto