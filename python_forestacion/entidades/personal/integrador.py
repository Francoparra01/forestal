"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/entidades/personal
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/__init__.py
# ================================================================================

"""
Entidades de gestión de personal.
"""

# ================================================================================
# ARCHIVO 2/5: apto_medico.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/apto_medico.py
# ================================================================================

"""
Entidad AptoMedico - Certificación médica.
"""

from datetime import date


class AptoMedico:
    """
    Representa una certificación médica para trabajo agrícola.
    
    Attributes:
        _fecha_emision: Fecha de emisión del apto
        _observaciones: Observaciones médicas
    """
    
    def __init__(self, fecha_emision: date, observaciones: str):
        """
        Inicializa un AptoMedico.
        
        Args:
            fecha_emision: Fecha de emisión
            observaciones: Observaciones médicas
        """
        self._fecha_emision = fecha_emision
        self._observaciones = observaciones
    
    def get_fecha_emision(self) -> date:
        """Retorna fecha de emisión."""
        return self._fecha_emision
    
    def set_fecha_emision(self, fecha: date) -> None:
        """Establece fecha de emisión."""
        self._fecha_emision = fecha
    
    def get_observaciones(self) -> str:
        """Retorna observaciones."""
        return self._observaciones
    
    def set_observaciones(self, observaciones: str) -> None:
        """Establece observaciones."""
        self._observaciones = observaciones
    
    def es_valido(self) -> bool:
        """
        Verifica si el apto médico es válido.
        
        Returns:
            True si fue emitido, False si no tiene fecha
        """
        return self._fecha_emision is not None

# ================================================================================
# ARCHIVO 3/5: herramienta.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/herramienta.py
# ================================================================================

"""
Entidad Herramienta - Equipamiento de trabajo.
"""


class Herramienta:
    """
    Representa una herramienta de trabajo.
    
    Attributes:
        _id: Identificador único
        _nombre: Nombre de la herramienta
        _certificacion_hs: Certificación de higiene y seguridad
    """
    
    def __init__(self, id_herramienta: int, nombre: str, certificacion_hs: str):
        """
        Inicializa una Herramienta.
        
        Args:
            id_herramienta: ID único
            nombre: Nombre descriptivo
            certificacion_hs: Certificación H&S
        """
        self._id = id_herramienta
        self._nombre = nombre
        self._certificacion_hs = certificacion_hs
    
    def get_id(self) -> int:
        """Retorna ID de la herramienta."""
        return self._id
    
    def set_id(self, id_herramienta: int) -> None:
        """Establece ID de la herramienta."""
        self._id = id_herramienta
    
    def get_nombre(self) -> str:
        """Retorna nombre de la herramienta."""
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """Establece nombre de la herramienta."""
        self._nombre = nombre
    
    def get_certificacion_hs(self) -> str:
        """Retorna certificación H&S."""
        return self._certificacion_hs
    
    def set_certificacion_hs(self, certificacion: str) -> None:
        """Establece certificación H&S."""
        self._certificacion_hs = certificacion

# ================================================================================
# ARCHIVO 4/5: tarea.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/tarea.py
# ================================================================================

"""
Entidad Tarea - Labor asignada.
"""

from datetime import date


class Tarea:
    """
    Representa una tarea agrícola.
    
    Attributes:
        _id: Identificador único
        _descripcion: Descripción de la tarea
        _fecha_programada: Fecha programada
        _completada: Estado de completitud
    """
    
    def __init__(self, id_tarea: int, descripcion: str, fecha_programada: date):
        """
        Inicializa una Tarea.
        
        Args:
            id_tarea: ID único
            descripcion: Descripción de la labor
            fecha_programada: Fecha programada
        """
        self._id = id_tarea
        self._descripcion = descripcion
        self._fecha_programada = fecha_programada
        self._completada = False
    
    def get_id(self) -> int:
        """Retorna ID de la tarea."""
        return self._id
    
    def set_id(self, id_tarea: int) -> None:
        """Establece ID de la tarea."""
        self._id = id_tarea
    
    def get_descripcion(self) -> str:
        """Retorna descripción."""
        return self._descripcion
    
    def set_descripcion(self, descripcion: str) -> None:
        """Establece descripción."""
        self._descripcion = descripcion
    
    def get_fecha_programada(self) -> date:
        """Retorna fecha programada."""
        return self._fecha_programada
    
    def set_fecha_programada(self, fecha: date) -> None:
        """Establece fecha programada."""
        self._fecha_programada = fecha
    
    def esta_completada(self) -> bool:
        """Retorna si está completada."""
        return self._completada
    
    def marcar_completada(self) -> None:
        """Marca la tarea como completada."""
        self._completada = True

# ================================================================================
# ARCHIVO 5/5: trabajador.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/trabajador.py
# ================================================================================

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

