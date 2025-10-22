"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/patrones/factory
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/factory/__init__.py
# ================================================================================

"""
Patrón Factory Method.
"""

# ================================================================================
# ARCHIVO 2/2: cultivo_factory.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/patrones/factory/cultivo_factory.py
# ================================================================================

"""
Factory Method para creación de cultivos.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoFactory:
    """
    Factory para crear cultivos sin conocer clases concretas.
    Implementa patrón Factory Method.
    """
    
    @staticmethod
    def crear_cultivo(especie: str) -> 'Cultivo':
        """
        Crea un cultivo según la especie especificada.
        
        Args:
            especie: Nombre de la especie ("Pino", "Olivo", "Lechuga", "Zanahoria")
            
        Returns:
            Instancia de Cultivo del tipo especificado
            
        Raises:
            ValueError: Si la especie no es reconocida
        """
        fabricas = {
            "Pino": CultivoFactory._crear_pino,
            "Olivo": CultivoFactory._crear_olivo,
            "Lechuga": CultivoFactory._crear_lechuga,
            "Zanahoria": CultivoFactory._crear_zanahoria
        }
        
        if especie not in fabricas:
            raise ValueError(f"Especie no soportada: {especie}")
        
        return fabricas[especie]()
    
    @staticmethod
    def _crear_pino() -> 'Cultivo':
        """Crea un Pino con configuración por defecto."""
        from python_forestacion.entidades.cultivos.pino import Pino
        return Pino(variedad="Parana")
    
    @staticmethod
    def _crear_olivo() -> 'Cultivo':
        """Crea un Olivo con configuración por defecto."""
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
        return Olivo(tipo_aceituna=TipoAceituna.ARBEQUINA)
    
    @staticmethod
    def _crear_lechuga() -> 'Cultivo':
        """Crea una Lechuga con configuración por defecto."""
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        return Lechuga(variedad="Criolla")
    
    @staticmethod
    def _crear_zanahoria() -> 'Cultivo':
        """Crea una Zanahoria con configuración por defecto."""
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        return Zanahoria(es_baby=False)

