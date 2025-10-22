"""
Excepción base del sistema.
"""


class ForestacionException(Exception):
    """
    Excepción base para todas las excepciones del dominio.
    
    Attributes:
        _user_message: Mensaje amigable para usuario
        _technical_message: Mensaje técnico para desarrollador
    """
    
    def __init__(self, user_message: str, technical_message: str):
        """
        Inicializa la excepción.
        
        Args:
            user_message: Mensaje para usuario final
            technical_message: Mensaje técnico detallado
        """
        super().__init__(user_message)
        self._user_message = user_message
        self._technical_message = technical_message
    
    def get_user_message(self) -> str:
        """Retorna mensaje amigable."""
        return self._user_message
    
    def get_technical_message(self) -> str:
        """Retorna mensaje técnico."""
        return self._technical_message
    
    def get_full_message(self) -> str:
        """Retorna mensaje completo."""
        return f"{self._user_message}\nDetalles tecnicos: {self._technical_message}"