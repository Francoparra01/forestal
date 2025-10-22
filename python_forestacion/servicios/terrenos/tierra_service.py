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