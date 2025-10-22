"""
Constantes centralizadas del sistema.
Todos los valores mágicos deben definirse aquí.
"""

# ===============================================
# CONSTANTES DE AGUA
# ===============================================
AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# ===============================================
# CONSTANTES DE RIEGO
# ===============================================
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50

# ===============================================
# CONSTANTES DE SENSORES
# ===============================================
TEMP_MIN_SENSOR = -25
TEMP_MAX_SENSOR = 50
HUMEDAD_MIN_SENSOR = 0
HUMEDAD_MAX_SENSOR = 100

# ===============================================
# INTERVALOS DE TIEMPO (segundos)
# ===============================================
INTERVALO_SENSOR_TEMPERATURA = 2
INTERVALO_SENSOR_HUMEDAD = 3
INTERVALO_CONTROL_RIEGO = 2.5

# ===============================================
# CONSTANTES DE CULTIVOS - PINO
# ===============================================
SUPERFICIE_PINO = 2.0
AGUA_INICIAL_PINO = 2
CRECIMIENTO_PINO = 0.10

# ===============================================
# CONSTANTES DE CULTIVOS - OLIVO
# ===============================================
SUPERFICIE_OLIVO = 1.5
AGUA_INICIAL_OLIVO = 3
CRECIMIENTO_OLIVO = 0.01

# ===============================================
# CONSTANTES DE CULTIVOS - LECHUGA
# ===============================================
SUPERFICIE_LECHUGA = 0.10
AGUA_INICIAL_LECHUGA = 1

# ===============================================
# CONSTANTES DE CULTIVOS - ZANAHORIA
# ===============================================
SUPERFICIE_ZANAHORIA = 0.15
AGUA_INICIAL_ZANAHORIA = 1

# ===============================================
# CONSTANTES DE ABSORCION
# ===============================================
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_LECHUGA = 1
ABSORCION_ZANAHORIA = 2

# ===============================================
# CONSTANTES DE ESTACIONES (hemisferio sur)
# ===============================================
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 3

# ===============================================
# CONSTANTES DE PERSISTENCIA
# ===============================================
DIRECTORIO_DATA = "data"
EXTENSION_ARCHIVO = ".dat"