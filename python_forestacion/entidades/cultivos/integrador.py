"""
Archivo integrador generado automaticamente
Directorio: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos
Fecha: 2025-10-22 02:06:45
Total de archivos integrados: 9
"""

# ================================================================================
# ARCHIVO 1/9: __init__.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/9: arbol.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/arbol.py
# ================================================================================

"""
Clase base para cultivos arbóreos.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Arbol(Cultivo):
    """
    Clase base para árboles.
    
    Attributes:
        _altura: Altura del árbol en metros
    """
    
    def __init__(self, agua: int, superficie: float, altura: float):
        """
        Inicializa un árbol.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie que ocupa en m2
            altura: Altura inicial en metros
        """
        super().__init__(agua, superficie)
        self._altura = altura
    
    def get_altura(self) -> float:
        """Retorna altura del árbol."""
        return self._altura
    
    def set_altura(self, altura: float) -> None:
        """Establece altura del árbol."""
        self._altura = altura

# ================================================================================
# ARCHIVO 3/9: cultivo.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/cultivo.py
# ================================================================================

"""
Interfaz base para todos los cultivos del sistema.
"""

from abc import ABC


class Cultivo(ABC):
    """
    Clase abstracta base para todos los cultivos.
    
    Attributes:
        _agua: Cantidad de agua en litros
        _superficie: Superficie ocupada en metros cuadrados
    """
    
    def __init__(self, agua: int, superficie: float):
        """
        Inicializa un cultivo.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie que ocupa en m2
        """
        self._agua = agua
        self._superficie = superficie
    
    def get_agua(self) -> int:
        """Retorna cantidad de agua del cultivo."""
        return self._agua
    
    def set_agua(self, agua: int) -> None:
        """Establece cantidad de agua del cultivo."""
        self._agua = agua
    
    def get_superficie(self) -> float:
        """Retorna superficie ocupada por el cultivo."""
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """Establece superficie del cultivo."""
        self._superficie = superficie

# ================================================================================
# ARCHIVO 4/9: hortaliza.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/hortaliza.py
# ================================================================================

"""
Clase base para cultivos hortícolas.
"""

from python_forestacion.entidades.cultivos.cultivo import Cultivo


class Hortaliza(Cultivo):
    """
    Clase base para hortalizas.
    
    Attributes:
        _invernadero: Indica si requiere invernadero
    """
    
    def __init__(self, agua: int, superficie: float, invernadero: bool):
        """
        Inicializa una hortaliza.
        
        Args:
            agua: Cantidad inicial de agua en litros
            superficie: Superficie que ocupa en m2
            invernadero: True si requiere invernadero
        """
        super().__init__(agua, superficie)
        self._invernadero = invernadero
    
    def get_invernadero(self) -> bool:
        """Retorna si requiere invernadero."""
        return self._invernadero
    
    def set_invernadero(self, invernadero: bool) -> None:
        """Establece requerimiento de invernadero."""
        self._invernadero = invernadero

# ================================================================================
# ARCHIVO 5/9: lechuga.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/lechuga.py
# ================================================================================

"""
Entidad Lechuga - Hortaliza de hoja.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_LECHUGA, SUPERFICIE_LECHUGA


class Lechuga(Hortaliza):
    """
    Representa una lechuga.
    
    Attributes:
        _variedad: Variedad de lechuga (Criolla, Romana, Mantecosa)
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa una Lechuga.
        
        Args:
            variedad: Variedad de lechuga
        """
        super().__init__(
            agua=AGUA_INICIAL_LECHUGA,
            superficie=SUPERFICIE_LECHUGA,
            invernadero=True
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """Retorna variedad de lechuga."""
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """Establece variedad de lechuga."""
        self._variedad = variedad

# ================================================================================
# ARCHIVO 6/9: olivo.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/olivo.py
# ================================================================================

"""
Entidad Olivo - Árbol frutal.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.entidades.cultivos.tipo_aceituna import TipoAceituna
from python_forestacion.constantes import AGUA_INICIAL_OLIVO, SUPERFICIE_OLIVO


class Olivo(Arbol):
    """
    Representa un árbol de Olivo.
    
    Attributes:
        _tipo_aceituna: Tipo de aceituna que produce
    """
    
    def __init__(self, tipo_aceituna: TipoAceituna):
        """
        Inicializa un Olivo.
        
        Args:
            tipo_aceituna: Tipo de aceituna
        """
        super().__init__(
            agua=AGUA_INICIAL_OLIVO,
            superficie=SUPERFICIE_OLIVO,
            altura=1.0
        )
        self._tipo_aceituna = tipo_aceituna
    
    def get_tipo_aceituna(self) -> TipoAceituna:
        """Retorna tipo de aceituna."""
        return self._tipo_aceituna
    
    def set_tipo_aceituna(self, tipo_aceituna: TipoAceituna) -> None:
        """Establece tipo de aceituna."""
        self._tipo_aceituna = tipo_aceituna

# ================================================================================
# ARCHIVO 7/9: pino.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/pino.py
# ================================================================================

"""
Entidad Pino - Árbol conífera.
"""

from python_forestacion.entidades.cultivos.arbol import Arbol
from python_forestacion.constantes import AGUA_INICIAL_PINO, SUPERFICIE_PINO


class Pino(Arbol):
    """
    Representa un árbol de Pino.
    
    Attributes:
        _variedad: Variedad del pino (Parana, Elliott, Taeda)
    """
    
    def __init__(self, variedad: str):
        """
        Inicializa un Pino.
        
        Args:
            variedad: Variedad del pino
        """
        super().__init__(
            agua=AGUA_INICIAL_PINO,
            superficie=SUPERFICIE_PINO,
            altura=0.5
        )
        self._variedad = variedad
    
    def get_variedad(self) -> str:
        """Retorna variedad del pino."""
        return self._variedad
    
    def set_variedad(self, variedad: str) -> None:
        """Establece variedad del pino."""
        self._variedad = variedad

# ================================================================================
# ARCHIVO 8/9: tipo_aceituna.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ================================================================================

"""
Enumeración de tipos de aceitunas.
"""

from enum import Enum


class TipoAceituna(Enum):
    """
    Tipos de aceitunas disponibles.
    """
    ARBEQUINA = "Arbequina"
    PICUAL = "Picual"
    MANZANILLA = "Manzanilla"

# ================================================================================
# ARCHIVO 9/9: zanahoria.py
# Ruta: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/zanahoria.py
# ================================================================================

"""
Entidad Zanahoria - Hortaliza de raíz.
"""

from python_forestacion.entidades.cultivos.hortaliza import Hortaliza
from python_forestacion.constantes import AGUA_INICIAL_ZANAHORIA, SUPERFICIE_ZANAHORIA


class Zanahoria(Hortaliza):
    """
    Representa una zanahoria.
    
    Attributes:
        _es_baby: Indica si es baby carrot
    """
    
    def __init__(self, es_baby: bool = False):
        """
        Inicializa una Zanahoria.
        
        Args:
            es_baby: True si es baby carrot
        """
        super().__init__(
            agua=AGUA_INICIAL_ZANAHORIA,
            superficie=SUPERFICIE_ZANAHORIA,
            invernadero=False
        )
        self._es_baby = es_baby
    
    def get_es_baby(self) -> bool:
        """Retorna si es baby carrot."""
        return self._es_baby
    
    def set_es_baby(self, es_baby: bool) -> None:
        """Establece si es baby carrot."""
        self._es_baby = es_baby

