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