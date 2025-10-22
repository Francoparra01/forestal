"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/parra1/diseno/forestal
Fecha de generacion: 2025-10-22 02:06:45
Total de archivos integrados: 69
Total de directorios procesados: 22
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. buscar_paquete.py
#   2. constantes.py
#   3. main.py
#
# DIRECTORIO: python_forestacion
#   4. __init__.py
#   5. constantes.py
#
# DIRECTORIO: python_forestacion/entidades
#   6. __init__.py
#
# DIRECTORIO: python_forestacion/entidades/cultivos
#   7. __init__.py
#   8. arbol.py
#   9. cultivo.py
#   10. hortaliza.py
#   11. lechuga.py
#   12. olivo.py
#   13. pino.py
#   14. tipo_aceituna.py
#   15. zanahoria.py
#
# DIRECTORIO: python_forestacion/entidades/personal
#   16. __init__.py
#   17. apto_medico.py
#   18. herramienta.py
#   19. tarea.py
#   20. trabajador.py
#
# DIRECTORIO: python_forestacion/entidades/terrenos
#   21. __init__.py
#   22. plantacion.py
#   23. registro_forestal.py
#   24. tierra.py
#
# DIRECTORIO: python_forestacion/excepciones
#   25. __init__.py
#   26. agua_agotada_exception.py
#   27. forestacion_exception.py
#   28. mensajes_exception.py
#   29. persistencia_exception.py
#   30. superficie_insuficiente_exception.py
#
# DIRECTORIO: python_forestacion/patrones
#   31. __init__.py
#
# DIRECTORIO: python_forestacion/patrones/factory
#   32. __init__.py
#   33. cultivo_factory.py
#
# DIRECTORIO: python_forestacion/patrones/observer
#   34. __init__.py
#   35. observable.py
#   36. observer.py
#
# DIRECTORIO: python_forestacion/patrones/observer/eventos
#   37. __init__.py
#   38. evento_plantacion.py
#   39. evento_sensor.py
#
# DIRECTORIO: python_forestacion/patrones/singleton
#   40. __init__.py
#
# DIRECTORIO: python_forestacion/patrones/strategy
#   41. __init__.py
#   42. absorcion_agua_strategy.py
#
# DIRECTORIO: python_forestacion/patrones/strategy/impl
#   43. __init__.py
#   44. absorcion_constante_strategy.py
#   45. absorcion_seasonal_strategy.py
#
# DIRECTORIO: python_forestacion/riego
#   46. __init__.py
#
# DIRECTORIO: python_forestacion/riego/control
#   47. __init__.py
#   48. control_riego_task.py
#
# DIRECTORIO: python_forestacion/riego/sensores
#   49. __init__.py
#   50. humedad_reader_task.py
#   51. temperatura_reader_task.py
#
# DIRECTORIO: python_forestacion/servicios
#   52. __init__.py
#
# DIRECTORIO: python_forestacion/servicios/cultivos
#   53. __init__.py
#   54. arbol_service.py
#   55. cultivo_service.py
#   56. cultivo_service_registry.py
#   57. lechuga_service.py
#   58. olivo_service.py
#   59. pino_service.py
#   60. zanahoria_service.py
#
# DIRECTORIO: python_forestacion/servicios/negocio
#   61. __init__.py
#   62. fincas_service.py
#   63. paquete.py
#
# DIRECTORIO: python_forestacion/servicios/personal
#   64. __init__.py
#   65. trabajador_service.py
#
# DIRECTORIO: python_forestacion/servicios/terrenos
#   66. __init__.py
#   67. plantacion_service.py
#   68. registro_forestal_service.py
#   69. tierra_service.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/69: buscar_paquete.py
# Directorio: .
# Ruta completa: /home/parra1/diseno/forestal/buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ==============================================================================
# ARCHIVO 2/69: constantes.py
# Directorio: .
# Ruta completa: /home/parra1/diseno/forestal/constantes.py
# ==============================================================================


AGUA_MINIMA = 10
AGUA_INICIAL_PLANTACION = 500

# Riego
TEMP_MIN_RIEGO = 8
TEMP_MAX_RIEGO = 15
HUMEDAD_MAX_RIEGO = 50
INTERVALO_CONTROL_RIEGO = 2.5
INTERVALO_SENSOR_TEMPERATURA = 2.0
INTERVALO_SENSOR_HUMEDAD = 3.0

# Estaciones
MES_INICIO_VERANO = 12
MES_FIN_VERANO = 2

# Absorción de agua
ABSORCION_SEASONAL_VERANO = 5
ABSORCION_SEASONAL_INVIERNO = 2
ABSORCION_CONSTANTE_LECHUGA = 1
ABSORCION_CONSTANTE_ZANAHORIA = 2

# Crecimiento
CRECIMIENTO_PINO_POR_RIEGO = 0.10
CRECIMIENTO_OLIVO_POR_RIEGO = 0.01

# Superficies (m²)
SUPERFICIE_PINO = 2.0
SUPERFICIE_OLIVO = 1.5
SUPERFICIE_LECHUGA = 0.5
SUPERFICIE_ZANAHORIA = 0.3

# Agua inicial por cultivo
AGUA_INICIAL_PINO = 2
AGUA_INICIAL_OLIVO = 2
AGUA_INICIAL_LECHUGA = 1
AGUA_INICIAL_ZANAHORIA = 1

# Altura inicial (metros)
ALTURA_INICIAL_PINO = 0.5
ALTURA_INICIAL_OLIVO = 1.0

# Sensores - Rangos
TEMP_MIN = -25.0
TEMP_MAX = 50.0
HUMEDAD_MIN = 0.0
HUMEDAD_MAX = 100.0

# Persistencia
DIRECTORIO_DATOS = "data"

# ==============================================================================
# ARCHIVO 3/69: main.py
# Directorio: .
# Ruta completa: /home/parra1/diseno/forestal/main.py
# ==============================================================================

"""
Sistema de Gestión Forestal - Punto de Entrada Principal
Demostración completa de patrones de diseño implementados.
"""

import time
from datetime import date, timedelta

from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
from python_forestacion.servicios.terrenos.registro_forestal_service import RegistroForestalService
from python_forestacion.servicios.personal.trabajador_service import TrabajadorService
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry

from python_forestacion.entidades.terrenos.registro_forestal import RegistroForestal
from python_forestacion.entidades.personal.trabajador import Trabajador
from python_forestacion.entidades.personal.herramienta import Herramienta
from python_forestacion.entidades.personal.tarea import Tarea
from python_forestacion.entidades.personal.apto_medico import AptoMedico

from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask


def imprimir_separador():
    """Imprime separador visual."""
    print("=" * 70)


def imprimir_seccion(titulo):
    """Imprime título de sección."""
    print("\n" + "-" * 70)
    print(f"  {titulo}")
    print("-" * 70)


def main():
    """Función principal que ejecuta demostración completa del sistema."""
    
    imprimir_separador()
    print("         SISTEMA DE GESTION FORESTAL - PATRONES DE DISENO")
    imprimir_separador()
    
    # PATRON SINGLETON
    imprimir_seccion("PATRON SINGLETON: Inicializando servicios")
    registry1 = CultivoServiceRegistry.get_instance()
    registry2 = CultivoServiceRegistry.get_instance()
    print(f"[OK] Registry 1 ID: {id(registry1)}")
    print(f"[OK] Registry 2 ID: {id(registry2)}")
    print(f"[OK] Son la misma instancia: {registry1 is registry2}")
    
    # CREACION DE INFRAESTRUCTURA
    imprimir_seccion("1. CREANDO INFRAESTRUCTURA TERRITORIAL")
    tierra_service = TierraService()
    terreno = tierra_service.crear_tierra_con_plantacion(
        id_padron_catastral=1,
        superficie=10000.0,
        domicilio="Valle de Uco, Mendoza",
        nombre_plantacion="La Consulta"
    )
    plantacion = terreno.get_finca()
    print(f"[OK] Tierra creada - Padron: {terreno.get_padron()}")
    print(f"[OK] Superficie total: {terreno.get_superficie()} m2")
    print(f"[OK] Plantacion: {plantacion.get_nombre()}")
    
    # PATRON FACTORY
    imprimir_seccion("2. PATRON FACTORY: Plantando cultivos")
    plantacion_service = PlantacionService()
    
    print("[INFO] Plantando 5 Pino(s)...")
    plantacion_service.plantar(plantacion, "Pino", 5)
    print("[OK] Pinos plantados exitosamente")
    
    print("[INFO] Plantando 3 Olivo(s)...")
    plantacion_service.plantar(plantacion, "Olivo", 3)
    print("[OK] Olivos plantados exitosamente")
    
    print("[INFO] Plantando 10 Lechuga(s)...")
    plantacion_service.plantar(plantacion, "Lechuga", 10)
    print("[OK] Lechugas plantadas exitosamente")
    
    print("[INFO] Plantando 8 Zanahoria(s)...")
    plantacion_service.plantar(plantacion, "Zanahoria", 8)
    print("[OK] Zanahorias plantadas exitosamente")
    
    print(f"\n[INFO] Superficie restante: {plantacion.get_superficie_disponible()} m2")
    print(f"[INFO] Total cultivos: {len(plantacion.get_cultivos())}")
    
    # PATRON OBSERVER - Sistema de riego
    imprimir_seccion("3. PATRON OBSERVER: Sistema de sensores")
    print("[INFO] Iniciando sensores ambientales...")
    
    sensor_temp = TemperaturaReaderTask()
    sensor_hum = HumedadReaderTask()
    
    controlador_riego = ControlRiegoTask(
        sensor_temp,
        sensor_hum,
        plantacion,
        plantacion_service
    )
    
    sensor_temp.start()
    sensor_hum.start()
    controlador_riego.start()
    
    print("[OK] Sensor de temperatura iniciado (2s intervalo)")
    print("[OK] Sensor de humedad iniciado (3s intervalo)")
    print("[OK] Controlador de riego iniciado (2.5s intervalo)")
    print("[INFO] Sistema automatizado funcionando por 15 segundos...")
    
    time.sleep(15)
    
    print("\n[INFO] Deteniendo sistema automatizado...")
    sensor_temp.detener()
    sensor_hum.detener()
    controlador_riego.detener()
    
    sensor_temp.join(timeout=5)
    sensor_hum.join(timeout=5)
    controlador_riego.join(timeout=5)
    
    print("[OK] Sistema detenido correctamente")
    
    # PATRON STRATEGY - Riego manual
    imprimir_seccion("4. PATRON STRATEGY: Riego con absorcion diferenciada")
    print(f"[INFO] Agua disponible antes: {plantacion.get_agua_disponible()} L")
    plantacion_service.regar(plantacion)
    print(f"[OK] Agua disponible despues: {plantacion.get_agua_disponible()} L")
    
    # GESTION DE PERSONAL
    imprimir_seccion("5. GESTION DE PERSONAL Y TAREAS")
    
    apto = AptoMedico(
        fecha_emision=date.today() - timedelta(days=30),
        observaciones="Apto para trabajo agricola"
    )
    
    tarea = Tarea(
        id_tarea=1,
        descripcion="Poda de arboles",
        fecha_programada=date.today()
    )
    
    trabajador = Trabajador(
        dni=12345678,
        nombre="Juan Martinez",
        tareas=[tarea],
        apto_medico=apto
    )
    
    plantacion.agregar_trabajador(trabajador)
    print(f"[OK] Trabajador {trabajador.get_nombre()} asignado")
    
    herramienta = Herramienta(
        id_herramienta=101,
        nombre="Tijera de podar",
        certificacion_hs="CERT-2024-101"
    )
    
    trabajador_service = TrabajadorService()
    exito = trabajador_service.trabajar(trabajador, date.today(), herramienta)
    
    if exito:
        print("[OK] Tareas ejecutadas correctamente")
    else:
        print("[ERROR] No se pudieron ejecutar las tareas")
    
    # COSECHA
    imprimir_seccion("6. COSECHA Y EMPAQUETADO")
    print("[INFO] Cosechando cultivos...")
    plantacion_service.cosechar(plantacion)
    print("[OK] Cosecha completada")
    
    # FUMIGACION
    print("\n[INFO] Aplicando fumigacion...")
    plantacion_service.fumigar(plantacion, "Insecticida organico")
    print("[OK] Fumigacion aplicada")
    
    # PERSISTENCIA
    imprimir_seccion("7. PERSISTENCIA DE DATOS")
    
    registro = RegistroForestal(
        id_padron=1,
        tierra=terreno,
        plantacion=plantacion,
        propietario="Maria Gonzalez",
        avaluo=85000000.50
    )
    
    registro_service = RegistroForestalService()
    
    print("[INFO] Guardando registro en disco...")
    registro_service.persistir(registro)
    print(f"[OK] Registro guardado: data/{registro.get_propietario()}.dat")
    
    print("\n[INFO] Recuperando registro desde disco...")
    registro_recuperado = RegistroForestalService.leer_registro("Maria Gonzalez")
    print("[OK] Registro recuperado exitosamente")
    
    print("\n[INFO] Datos del registro:")
    registro_service.mostrar_datos(registro_recuperado)
    
    # RESUMEN FINAL
    imprimir_separador()
    print("              EJEMPLO COMPLETADO EXITOSAMENTE")
    imprimir_separador()
    print("  [OK] SINGLETON   - CultivoServiceRegistry (instancia unica)")
    print("  [OK] FACTORY     - Creacion de 4 tipos de cultivos")
    print("  [OK] OBSERVER    - Sistema de sensores y notificaciones")
    print("  [OK] STRATEGY    - Algoritmos de absorcion diferenciados")
    print("  [OK] REGISTRY    - Dispatch polimorfico sin isinstance")
    imprimir_separador()
    print()


if __name__ == "__main__":
    main()


################################################################################
# DIRECTORIO: python_forestacion
################################################################################

# ==============================================================================
# ARCHIVO 4/69: __init__.py
# Directorio: python_forestacion
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/__init__.py
# ==============================================================================

"""
Paquete principal del Sistema de Gestión Forestal.
"""

__version__ = "1.0.0"
__author__ = "Sistema Forestal"

# ==============================================================================
# ARCHIVO 5/69: constantes.py
# Directorio: python_forestacion
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/constantes.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_forestacion/entidades
################################################################################

# ==============================================================================
# ARCHIVO 6/69: __init__.py
# Directorio: python_forestacion/entidades
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/__init__.py
# ==============================================================================

"""
Entidades de gestión territorial.
"""


################################################################################
# DIRECTORIO: python_forestacion/entidades/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 7/69: __init__.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 8/69: arbol.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/arbol.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/69: cultivo.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/cultivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 10/69: hortaliza.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/hortaliza.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 11/69: lechuga.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/lechuga.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 12/69: olivo.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/olivo.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 13/69: pino.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/pino.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 14/69: tipo_aceituna.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/tipo_aceituna.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/69: zanahoria.py
# Directorio: python_forestacion/entidades/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/cultivos/zanahoria.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_forestacion/entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 16/69: __init__.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/__init__.py
# ==============================================================================

"""
Entidades de gestión de personal.
"""

# ==============================================================================
# ARCHIVO 17/69: apto_medico.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/apto_medico.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 18/69: herramienta.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/herramienta.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 19/69: tarea.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/tarea.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 20/69: trabajador.py
# Directorio: python_forestacion/entidades/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/personal/trabajador.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_forestacion/entidades/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 21/69: __init__.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 22/69: plantacion.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/plantacion.py
# ==============================================================================

"""
Entidad Plantación - Agrupación de cultivos.
"""

from typing import List, TYPE_CHECKING

from python_forestacion.constantes import AGUA_INICIAL_PLANTACION

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.personal.trabajador import Trabajador


class Plantacion:
    """
    Representa una plantación agrícola.
    
    Attributes:
        _nombre: Nombre identificatorio
        _superficie_disponible: Superficie libre en m2
        _cultivos: Lista de cultivos plantados
        _agua_disponible: Agua disponible en litros
        _trabajadores: Personal asignado
    """
    
    def __init__(self, nombre: str, superficie_total: float):
        """
        Inicializa una Plantación.
        
        Args:
            nombre: Nombre de la plantación
            superficie_total: Superficie total en m2
        """
        self._nombre = nombre
        self._superficie_disponible = superficie_total
        self._cultivos: List['Cultivo'] = []
        self._agua_disponible = AGUA_INICIAL_PLANTACION
        self._trabajadores: List['Trabajador'] = []
    
    def get_nombre(self) -> str:
        """Retorna nombre de la plantación."""
        return self._nombre
    
    def set_nombre(self, nombre: str) -> None:
        """Establece nombre de la plantación."""
        self._nombre = nombre
    
    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible
    
    def set_superficie_disponible(self, superficie: float) -> None:
        """Establece superficie disponible."""
        self._superficie_disponible = superficie
    
    def get_cultivos(self) -> List['Cultivo']:
        """Retorna lista de cultivos (copia defensiva)."""
        return self._cultivos.copy()
    
    def agregar_cultivo(self, cultivo: 'Cultivo') -> None:
        """Agrega un cultivo a la plantación."""
        self._cultivos.append(cultivo)
    
    def get_agua_disponible(self) -> int:
        """Retorna agua disponible."""
        return self._agua_disponible
    
    def set_agua_disponible(self, agua: int) -> None:
        """Establece agua disponible."""
        self._agua_disponible = agua
    
    def get_trabajadores(self) -> List['Trabajador']:
        """Retorna lista de trabajadores (copia defensiva)."""
        return self._trabajadores.copy()
    
    def agregar_trabajador(self, trabajador: 'Trabajador') -> None:
        """Agrega un trabajador a la plantación."""
        self._trabajadores.append(trabajador)

# ==============================================================================
# ARCHIVO 23/69: registro_forestal.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/registro_forestal.py
# ==============================================================================

"""
Entidad RegistroForestal - Registro legal completo.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.tierra import Tierra
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class RegistroForestal:
    """
    Representa un registro forestal legal completo.
    
    Attributes:
        _id_padron: Identificador de padrón
        _tierra: Parcela catastral
        _plantacion: Plantación asociada
        _propietario: Nombre del propietario
        _avaluo: Avalúo fiscal
    """
    
    def __init__(
        self,
        id_padron: int,
        tierra: 'Tierra',
        plantacion: 'Plantacion',
        propietario: str,
        avaluo: float
    ):
        """
        Inicializa un RegistroForestal.
        
        Args:
            id_padron: Identificador de padrón
            tierra: Tierra asociada
            plantacion: Plantación asociada
            propietario: Nombre del propietario
            avaluo: Avalúo fiscal en pesos
        """
        self._id_padron = id_padron
        self._tierra = tierra
        self._plantacion = plantacion
        self._propietario = propietario
        self._avaluo = avaluo
    
    def get_id_padron(self) -> int:
        """Retorna ID de padrón."""
        return self._id_padron
    
    def set_id_padron(self, id_padron: int) -> None:
        """Establece ID de padrón."""
        self._id_padron = id_padron
    
    def get_tierra(self) -> 'Tierra':
        """Retorna tierra asociada."""
        return self._tierra
    
    def set_tierra(self, tierra: 'Tierra') -> None:
        """Establece tierra asociada."""
        self._tierra = tierra
    
    def get_plantacion(self) -> 'Plantacion':
        """Retorna plantación asociada."""
        return self._plantacion
    
    def set_plantacion(self, plantacion: 'Plantacion') -> None:
        """Establece plantación asociada."""
        self._plantacion = plantacion
    
    def get_propietario(self) -> str:
        """Retorna nombre del propietario."""
        return self._propietario
    
    def set_propietario(self, propietario: str) -> None:
        """Establece nombre del propietario."""
        self._propietario = propietario
    
    def get_avaluo(self) -> float:
        """Retorna avalúo fiscal."""
        return self._avaluo
    
    def set_avaluo(self, avaluo: float) -> None:
        """Establece avalúo fiscal."""
        self._avaluo = avaluo

# ==============================================================================
# ARCHIVO 24/69: tierra.py
# Directorio: python_forestacion/entidades/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/entidades/terrenos/tierra.py
# ==============================================================================

"""
Entidad Tierra - Parcela catastral.
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class Tierra:
    """
    Representa una parcela de tierra catastral.
    
    Attributes:
        _padron: Número de padrón catastral único
        _superficie: Superficie en metros cuadrados
        _domicilio: Ubicación geográfica
        _finca: Plantación asociada
    """
    
    def __init__(
        self,
        padron: int,
        superficie: float,
        domicilio: str,
        finca: 'Plantacion'
    ):
        """
        Inicializa una Tierra.
        
        Args:
            padron: Número de padrón catastral
            superficie: Superficie en m2
            domicilio: Dirección de ubicación
            finca: Plantación asociada
        """
        self._padron = padron
        self._superficie = superficie
        self._domicilio = domicilio
        self._finca = finca
    
    def get_padron(self) -> int:
        """Retorna número de padrón."""
        return self._padron
    
    def set_padron(self, padron: int) -> None:
        """Establece número de padrón."""
        self._padron = padron
    
    def get_superficie(self) -> float:
        """Retorna superficie."""
        return self._superficie
    
    def set_superficie(self, superficie: float) -> None:
        """Establece superficie."""
        self._superficie = superficie
    
    def get_domicilio(self) -> str:
        """Retorna domicilio."""
        return self._domicilio
    
    def set_domicilio(self, domicilio: str) -> None:
        """Establece domicilio."""
        self._domicilio = domicilio
    
    def get_finca(self) -> 'Plantacion':
        """Retorna plantación asociada."""
        return self._finca
    
    def set_finca(self, finca: 'Plantacion') -> None:
        """Establece plantación asociada."""
        self._finca = finca


################################################################################
# DIRECTORIO: python_forestacion/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 25/69: __init__.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/excepciones/__init__.py
# ==============================================================================

"""
Excepciones personalizadas del sistema.
"""

# ==============================================================================
# ARCHIVO 26/69: agua_agotada_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/excepciones/agua_agotada_exception.py
# ==============================================================================

"""
Excepción cuando no hay agua suficiente.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_AGUA_AGOTADA_USER,
    MSG_AGUA_AGOTADA_TECH
)


class AguaAgotadaException(ForestacionException):
    """
    Excepción lanzada cuando no hay agua disponible.
    
    Attributes:
        _agua_requerida: Agua necesaria
        _agua_disponible: Agua disponible actual
    """
    
    def __init__(self, agua_requerida: int, agua_disponible: int):
        """
        Inicializa la excepción.
        
        Args:
            agua_requerida: Agua necesaria en litros
            agua_disponible: Agua disponible en litros
        """
        user_msg = MSG_AGUA_AGOTADA_USER
        tech_msg = (
            f"{MSG_AGUA_AGOTADA_TECH}: "
            f"requerida={agua_requerida}L, disponible={agua_disponible}L"
        )
        super().__init__(user_msg, tech_msg)
        
        self._agua_requerida = agua_requerida
        self._agua_disponible = agua_disponible
    
    def get_agua_requerida(self) -> int:
        """Retorna agua requerida."""
        return self._agua_requerida
    
    def get_agua_disponible(self) -> int:
        """Retorna agua disponible."""
        return self._agua_disponible

# ==============================================================================
# ARCHIVO 27/69: forestacion_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/excepciones/forestacion_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 28/69: mensajes_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/excepciones/mensajes_exception.py
# ==============================================================================

"""
Mensajes centralizados para excepciones.
"""

# Mensajes de SuperficieInsuficienteException
MSG_SUPERFICIE_INSUFICIENTE_USER = "No hay suficiente superficie disponible para plantar"
MSG_SUPERFICIE_INSUFICIENTE_TECH = "Superficie requerida excede disponible"

# Mensajes de AguaAgotadaException
MSG_AGUA_AGOTADA_USER = "No hay suficiente agua disponible para regar"
MSG_AGUA_AGOTADA_TECH = "Agua requerida excede disponible"

# Mensajes de PersistenciaException
MSG_PERSISTENCIA_ERROR_USER = "Error al guardar o recuperar datos"
MSG_PERSISTENCIA_ERROR_TECH = "Fallo en operacion de serializacion"

# ==============================================================================
# ARCHIVO 29/69: persistencia_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/excepciones/persistencia_exception.py
# ==============================================================================

"""
Excepción de errores de persistencia.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_PERSISTENCIA_ERROR_USER,
    MSG_PERSISTENCIA_ERROR_TECH
)


class PersistenciaException(ForestacionException):
    """
    Excepción lanzada en errores de persistencia.
    """
    
    def __init__(self, detalle: str):
        """
        Inicializa la excepción.
        
        Args:
            detalle: Detalle del error
        """
        user_msg = MSG_PERSISTENCIA_ERROR_USER
        tech_msg = f"{MSG_PERSISTENCIA_ERROR_TECH}: {detalle}"
        super().__init__(user_msg, tech_msg)

# ==============================================================================
# ARCHIVO 30/69: superficie_insuficiente_exception.py
# Directorio: python_forestacion/excepciones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/excepciones/superficie_insuficiente_exception.py
# ==============================================================================

"""
Excepción cuando no hay superficie suficiente.
"""

from python_forestacion.excepciones.forestacion_exception import ForestacionException
from python_forestacion.excepciones.mensajes_exception import (
    MSG_SUPERFICIE_INSUFICIENTE_USER,
    MSG_SUPERFICIE_INSUFICIENTE_TECH
)


class SuperficieInsuficienteException(ForestacionException):
    """
    Excepción lanzada cuando no hay superficie disponible.
    
    Attributes:
        _superficie_requerida: Superficie necesaria
        _superficie_disponible: Superficie disponible actual
    """
    
    def __init__(self, superficie_requerida: float, superficie_disponible: float):
        """
        Inicializa la excepción.
        
        Args:
            superficie_requerida: Superficie necesaria en m2
            superficie_disponible: Superficie disponible en m2
        """
        user_msg = MSG_SUPERFICIE_INSUFICIENTE_USER
        tech_msg = (
            f"{MSG_SUPERFICIE_INSUFICIENTE_TECH}: "
            f"requerida={superficie_requerida}, disponible={superficie_disponible}"
        )
        super().__init__(user_msg, tech_msg)
        
        self._superficie_requerida = superficie_requerida
        self._superficie_disponible = superficie_disponible
    
    def get_superficie_requerida(self) -> float:
        """Retorna superficie requerida."""
        return self._superficie_requerida
    
    def get_superficie_disponible(self) -> float:
        """Retorna superficie disponible."""
        return self._superficie_disponible


################################################################################
# DIRECTORIO: python_forestacion/patrones
################################################################################

# ==============================================================================
# ARCHIVO 31/69: __init__.py
# Directorio: python_forestacion/patrones
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/__init__.py
# ==============================================================================

"""
Implementaciones de patrones de diseño.
"""


################################################################################
# DIRECTORIO: python_forestacion/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 32/69: __init__.py
# Directorio: python_forestacion/patrones/factory
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/factory/__init__.py
# ==============================================================================

"""
Patrón Factory Method.
"""

# ==============================================================================
# ARCHIVO 33/69: cultivo_factory.py
# Directorio: python_forestacion/patrones/factory
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/factory/cultivo_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_forestacion/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 34/69: __init__.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/__init__.py
# ==============================================================================

"""
Patrón Observer.
"""

# ==============================================================================
# ARCHIVO 35/69: observable.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/observable.py
# ==============================================================================

"""
Clase base Observable para patrón Observer.
"""

from abc import ABC
from typing import Generic, TypeVar, List

from python_forestacion.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(ABC, Generic[T]):
    """
    Clase base para objetos observables tipo-seguros.
    
    Type Parameters:
        T: Tipo del evento que notifica
    """
    
    def __init__(self):
        """Inicializa lista de observadores."""
        self._observadores: List[Observer[T]] = []
    
    def agregar_observador(self, observador: Observer[T]) -> None:
        """
        Agrega un observador.
        
        Args:
            observador: Observador a agregar
        """
        self._observadores.append(observador)
    
    def eliminar_observador(self, observador: Observer[T]) -> None:
        """
        Elimina un observador.
        
        Args:
            observador: Observador a eliminar
        """
        self._observadores.remove(observador)
    
    def notificar_observadores(self, evento: T) -> None:
        """
        Notifica a todos los observadores.
        
        Args:
            evento: Dato del evento a notificar
        """
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 36/69: observer.py
# Directorio: python_forestacion/patrones/observer
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/observer.py
# ==============================================================================

"""
Interfaz Observer para patrón Observer.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')


class Observer(ABC, Generic[T]):
    """
    Interfaz para observadores tipo-seguros.
    
    Type Parameters:
        T: Tipo del evento que observa
    """
    
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        """
        Método llamado cuando el observable notifica un cambio.
        
        Args:
            evento: Dato del evento
        """
        pass


################################################################################
# DIRECTORIO: python_forestacion/patrones/observer/eventos
################################################################################

# ==============================================================================
# ARCHIVO 37/69: __init__.py
# Directorio: python_forestacion/patrones/observer/eventos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos/__init__.py
# ==============================================================================

"""
Eventos del sistema.
"""

# ==============================================================================
# ARCHIVO 38/69: evento_plantacion.py
# Directorio: python_forestacion/patrones/observer/eventos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos/evento_plantacion.py
# ==============================================================================

"""
Evento de operaciones en plantación.
"""


class EventoPlantacion:
    """
    Representa un evento operativo en plantación.
    
    Attributes:
        _tipo: Tipo de evento ("riego", "cosecha", "fumigacion")
        _descripcion: Descripción del evento
    """
    
    def __init__(self, tipo: str, descripcion: str):
        """
        Inicializa un EventoPlantacion.
        
        Args:
            tipo: Tipo de evento
            descripcion: Descripción detallada
        """
        self._tipo = tipo
        self._descripcion = descripcion
    
    def get_tipo(self) -> str:
        """Retorna tipo de evento."""
        return self._tipo
    
    def get_descripcion(self) -> str:
        """Retorna descripción."""
        return self._descripcion

# ==============================================================================
# ARCHIVO 39/69: evento_sensor.py
# Directorio: python_forestacion/patrones/observer/eventos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/observer/eventos/evento_sensor.py
# ==============================================================================

"""
Evento de sensores ambientales.
"""


class EventoSensor:
    """
    Representa un evento de lectura de sensor.
    
    Attributes:
        _tipo: Tipo de sensor ("temperatura" o "humedad")
        _valor: Valor leído
    """
    
    def __init__(self, tipo: str, valor: float):
        """
        Inicializa un EventoSensor.
        
        Args:
            tipo: Tipo de sensor
            valor: Valor leído
        """
        self._tipo = tipo
        self._valor = valor
    
    def get_tipo(self) -> str:
        """Retorna tipo de sensor."""
        return self._tipo
    
    def get_valor(self) -> float:
        """Retorna valor leído."""
        return self._valor


################################################################################
# DIRECTORIO: python_forestacion/patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 40/69: __init__.py
# Directorio: python_forestacion/patrones/singleton
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/singleton/__init__.py
# ==============================================================================

"""
Patrón Singleton.
"""


################################################################################
# DIRECTORIO: python_forestacion/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 41/69: __init__.py
# Directorio: python_forestacion/patrones/strategy
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/__init__.py
# ==============================================================================

"""
Patrón Strategy.
"""

# ==============================================================================
# ARCHIVO 42/69: absorcion_agua_strategy.py
# Directorio: python_forestacion/patrones/strategy
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/absorcion_agua_strategy.py
# ==============================================================================

"""
Interfaz Strategy para absorción de agua.
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionAguaStrategy(ABC):
    """
    Interfaz para estrategias de absorción de agua.
    Implementa patrón Strategy.
    """
    
    @abstractmethod
    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: 'Cultivo'
    ) -> int:
        """
        Calcula cantidad de agua a absorber.
        
        Args:
            fecha: Fecha actual
            temperatura: Temperatura ambiente en °C
            humedad: Humedad relativa en %
            cultivo: Cultivo que absorbe
            
        Returns:
            Cantidad de agua en litros
        """
        pass


################################################################################
# DIRECTORIO: python_forestacion/patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 43/69: __init__.py
# Directorio: python_forestacion/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl/__init__.py
# ==============================================================================

"""
Implementaciones concretas de estrategias.
"""

# ==============================================================================
# ARCHIVO 44/69: absorcion_constante_strategy.py
# Directorio: python_forestacion/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl/absorcion_constante_strategy.py
# ==============================================================================

"""
Estrategia de absorción constante.
"""

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionConstanteStrategy(AbsorcionAguaStrategy):
    """
    Estrategia con absorción constante independiente de la estación.
    Usada para hortalizas (Lechuga, Zanahoria).
    """

    def __init__(self, cantidad_constante: float = 0.4):
        """
        Inicializa la estrategia.

        Args:
            cantidad_constante: Litros constantes a absorber.
        """
        self._cantidad = float(cantidad_constante)

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: "Cultivo",
    ) -> float:
        """
        Retorna una cantidad constante de agua absorbida.

        Args:
            fecha: No usado en esta estrategia.
            temperatura: No usado.
            humedad: No usado.
            cultivo: Cultivo que absorbe.

        Returns:
            Litros constantes de agua absorbidos.
        """
        return self._cantidad



# ==============================================================================
# ARCHIVO 45/69: absorcion_seasonal_strategy.py
# Directorio: python_forestacion/patrones/strategy/impl
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/patrones/strategy/impl/absorcion_seasonal_strategy.py
# ==============================================================================

"""
Estrategia de absorción estacional.
"""

from datetime import date
from typing import TYPE_CHECKING
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class AbsorcionSeasonalStrategy(AbsorcionAguaStrategy):
    """
    Estrategia de absorción de agua que varía según la temperatura y la humedad.
    Usada para árboles (Pino, Olivo).
    """

    def calcular_absorcion(
        self,
        fecha: date,
        temperatura: float,
        humedad: float,
        cultivo: "Cultivo",
    ) -> float:
        """
        Calcula la cantidad de agua absorbida según estación simulada.
        A mayor temperatura y menor humedad, más absorción.

        Args:
            fecha: Fecha actual (se puede usar para estacionalidad)
            temperatura: Temperatura ambiente en °C
            humedad: Humedad relativa (0–1)
            cultivo: Cultivo que absorbe

        Returns:
            Litros de agua absorbidos.
        """
        base = 0.5  # L/h de referencia
        factor_temp = max(0.0, (temperatura - 10.0)) * 0.03
        factor_humedad = max(0.0, 1.0 - min(1.0, humedad))
        return base * (1.0 + factor_temp) * (1.0 + 0.5 * factor_humedad)

        return self._cantidad



################################################################################
# DIRECTORIO: python_forestacion/riego
################################################################################

# ==============================================================================
# ARCHIVO 46/69: __init__.py
# Directorio: python_forestacion/riego
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/riego/__init__.py
# ==============================================================================

"""
Sistema de riego automatizado.
"""


################################################################################
# DIRECTORIO: python_forestacion/riego/control
################################################################################

# ==============================================================================
# ARCHIVO 47/69: __init__.py
# Directorio: python_forestacion/riego/control
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/riego/control/__init__.py
# ==============================================================================

"""
Control de riego automatizado.
"""

# ==============================================================================
# ARCHIVO 48/69: control_riego_task.py
# Directorio: python_forestacion/riego/control
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/riego/control/control_riego_task.py
# ==============================================================================

"""
Controlador de riego (Observer).
"""

import threading
import time
from typing import TYPE_CHECKING

from python_forestacion.patrones.observer.observer import Observer
from python_forestacion.constantes import (
    INTERVALO_CONTROL_RIEGO,
    TEMP_MIN_RIEGO,
    TEMP_MAX_RIEGO,
    HUMEDAD_MAX_RIEGO
)

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion
    from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService
    from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
    from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask


class ControlRiegoTask(threading.Thread, Observer[float]):
    """
    Thread que controla riego automático basado en sensores.
    Implementa patrón Observer como Observer.
    """
    
    def __init__(
        self,
        sensor_temperatura: 'TemperaturaReaderTask',
        sensor_humedad: 'HumedadReaderTask',
        plantacion: 'Plantacion',
        plantacion_service: 'PlantacionService'
    ):
        """
        Inicializa controlador de riego.
        
        Args:
            sensor_temperatura: Sensor de temperatura a observar
            sensor_humedad: Sensor de humedad a observar
            plantacion: Plantación a regar
            plantacion_service: Servicio de plantación
        """
        threading.Thread.__init__(self, daemon=True)
        
        self._plantacion = plantacion
        self._plantacion_service = plantacion_service
        
        self._ultima_temperatura = 20.0
        self._ultima_humedad = 50.0
        
        self._detenido = threading.Event()
        
        # Suscribirse a sensores (Observer pattern)
        sensor_temperatura.agregar_observador(self)
        sensor_humedad.agregar_observador(self)
    
    def actualizar(self, evento: float) -> None:
        """
        Método del Observer - recibe notificaciones de sensores.
        
        Args:
            evento: Valor del sensor (temperatura o humedad)
        """
        # Determinar si es temperatura o humedad por rango
        if -25 <= evento <= 50:  # Rango de temperatura
            self._ultima_temperatura = evento
        else:  # Rango de humedad
            self._ultima_humedad = evento
    
    def run(self):
        """
        Bucle principal del controlador.
        Evalúa condiciones cada INTERVALO_CONTROL_RIEGO segundos.
        """
        while not self._detenido.is_set():
            self._evaluar_y_regar()
            time.sleep(INTERVALO_CONTROL_RIEGO)
    
    def _evaluar_y_regar(self):
        """
        Evalúa condiciones y riega si se cumplen.
        
        Condiciones para riego:
        - TEMP_MIN_RIEGO <= temperatura <= TEMP_MAX_RIEGO
        - humedad < HUMEDAD_MAX_RIEGO
        """
        temp_ok = TEMP_MIN_RIEGO <= self._ultima_temperatura <= TEMP_MAX_RIEGO
        humedad_ok = self._ultima_humedad < HUMEDAD_MAX_RIEGO
        
        if temp_ok and humedad_ok:
            try:
                self._plantacion_service.regar(self._plantacion)
                print(f"[RIEGO] T={self._ultima_temperatura:.1f}C, "
                      f"H={self._ultima_humedad:.1f}% -> RIEGO ACTIVADO")
            except Exception as e:
                print(f"[ERROR] Fallo en riego: {e}")
    
    def detener(self):
        """Detiene el thread de forma controlada."""
        self._detenido.set()


################################################################################
# DIRECTORIO: python_forestacion/riego/sensores
################################################################################

# ==============================================================================
# ARCHIVO 49/69: __init__.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/riego/sensores/__init__.py
# ==============================================================================

"""
Sensores ambientales.
"""

# ==============================================================================
# ARCHIVO 50/69: humedad_reader_task.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/riego/sensores/humedad_reader_task.py
# ==============================================================================

"""
Sensor de humedad (Observable).
"""

import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_HUMEDAD,
    HUMEDAD_MIN_SENSOR,
    HUMEDAD_MAX_SENSOR
)


class HumedadReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee humedad y notifica a observadores.
    Implementa patrón Observer como Observable.
    """
    
    def __init__(self):
        """Inicializa sensor de humedad."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self):
        """
        Bucle principal del sensor.
        Lee humedad cada INTERVALO_SENSOR_HUMEDAD segundos.
        """
        while not self._detenido.is_set():
            humedad = self._leer_humedad()
            self.notificar_observadores(humedad)
            time.sleep(INTERVALO_SENSOR_HUMEDAD)
    
    def _leer_humedad(self) -> float:
        """
        Simula lectura de sensor de humedad.
        
        Returns:
            Humedad relativa en %
        """
        return random.uniform(HUMEDAD_MIN_SENSOR, HUMEDAD_MAX_SENSOR)
    
    def detener(self):
        """Detiene el thread de forma controlada."""
        self._detenido.set()

# ==============================================================================
# ARCHIVO 51/69: temperatura_reader_task.py
# Directorio: python_forestacion/riego/sensores
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/riego/sensores/temperatura_reader_task.py
# ==============================================================================

"""
Sensor de temperatura (Observable).
"""

import threading
import time
import random

from python_forestacion.patrones.observer.observable import Observable
from python_forestacion.constantes import (
    INTERVALO_SENSOR_TEMPERATURA,
    TEMP_MIN_SENSOR,
    TEMP_MAX_SENSOR
)


class TemperaturaReaderTask(threading.Thread, Observable[float]):
    """
    Thread que lee temperatura y notifica a observadores.
    Implementa patrón Observer como Observable.
    """
    
    def __init__(self):
        """Inicializa sensor de temperatura."""
        threading.Thread.__init__(self, daemon=True)
        Observable.__init__(self)
        self._detenido = threading.Event()
    
    def run(self):
        """
        Bucle principal del sensor.
        Lee temperatura cada INTERVALO_SENSOR_TEMPERATURA segundos.
        """
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            self.notificar_observadores(temperatura)
            time.sleep(INTERVALO_SENSOR_TEMPERATURA)
    
    def _leer_temperatura(self) -> float:
        """
        Simula lectura de sensor de temperatura.
        
        Returns:
            Temperatura en °C
        """
        return random.uniform(TEMP_MIN_SENSOR, TEMP_MAX_SENSOR)
    
    def detener(self):
        """Detiene el thread de forma controlada."""
        self._detenido.set()


################################################################################
# DIRECTORIO: python_forestacion/servicios
################################################################################

# ==============================================================================
# ARCHIVO 52/69: __init__.py
# Directorio: python_forestacion/servicios
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/__init__.py
# ==============================================================================

"""
Servicios del sistema con lógica de negocio.
"""


################################################################################
# DIRECTORIO: python_forestacion/servicios/cultivos
################################################################################

# ==============================================================================
# ARCHIVO 53/69: __init__.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/__init__.py
# ==============================================================================

"""
Servicios de gestión de cultivos.
"""

# ==============================================================================
# ARCHIVO 54/69: arbol_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/arbol_service.py
# ==============================================================================

"""
Servicio base para árboles.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.arbol import Arbol


class ArbolService(CultivoService):
    """
    Servicio base para árboles.
    Extiende CultivoService con operaciones específicas de árboles.
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa servicio de árbol.
        
        Args:
            estrategia: Estrategia de absorción
        """
        super().__init__(estrategia)
    
    def mostrar_datos(self, arbol: 'Arbol') -> None:
        """
        Muestra datos del árbol incluyendo altura.
        
        Args:
            arbol: Árbol a mostrar
        """
        super().mostrar_datos(arbol)
        print(f"Altura: {arbol.get_altura():.2f} m")

# ==============================================================================
# ARCHIVO 55/69: cultivo_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/cultivo_service.py
# ==============================================================================

"""
Servicio base para cultivos.
"""

from datetime import date
from typing import TYPE_CHECKING

from python_forestacion.patrones.strategy.absorcion_agua_strategy import AbsorcionAguaStrategy

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo


class CultivoService:
    """
    Servicio base para operaciones sobre cultivos.
    
    Attributes:
        _estrategia: Estrategia de absorción de agua
    """
    
    def __init__(self, estrategia: AbsorcionAguaStrategy):
        """
        Inicializa servicio.
        
        Args:
            estrategia: Estrategia de absorción inyectada
        """
        self._estrategia = estrategia
    
    def absorver_agua(
        self,
        cultivo: 'Cultivo',
        fecha: date = None,
        temperatura: float = 20.0,
        humedad: float = 50.0
    ) -> int:
        """
        Calcula y aplica absorción de agua usando Strategy.
        
        Args:
            cultivo: Cultivo que absorbe
            fecha: Fecha actual (default: hoy)
            temperatura: Temperatura ambiente
            humedad: Humedad relativa
            
        Returns:
            Litros absorbidos
        """
        if fecha is None:
            fecha = date.today()
        
        cantidad = self._estrategia.calcular_absorcion(
            fecha, temperatura, humedad, cultivo
        )
        
        agua_actual = cultivo.get_agua()
        cultivo.set_agua(agua_actual + cantidad)
        
        return cantidad
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Muestra datos del cultivo.
        
        Args:
            cultivo: Cultivo a mostrar
        """
        print(f"Agua: {cultivo.get_agua()} L")
        print(f"Superficie: {cultivo.get_superficie()} m2")

# ==============================================================================
# ARCHIVO 56/69: cultivo_service_registry.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/cultivo_service_registry.py
# ==============================================================================

"""
Registry de servicios de cultivos (Singleton + Registry Pattern).
"""

from threading import Lock
from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.pino_service import PinoService
from python_forestacion.servicios.cultivos.olivo_service import OlivoService
from python_forestacion.servicios.cultivos.lechuga_service import LechugaService
from python_forestacion.servicios.cultivos.zanahoria_service import ZanahoriaService

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.cultivo import Cultivo
    from python_forestacion.entidades.cultivos.pino import Pino
    from python_forestacion.entidades.cultivos.olivo import Olivo
    from python_forestacion.entidades.cultivos.lechuga import Lechuga
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class CultivoServiceRegistry:
    """
    Registry de servicios con patrón Singleton.
    Elimina instanceof mediante dispatch polimórfico.
    
    Thread-safe con double-checked locking.
    """
    
    _instance = None
    _lock = Lock()
    
    def __new__(cls):
        """
        Implementa Singleton thread-safe.
        
        Returns:
            Instancia única del registry
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._inicializar()
        return cls._instance
    
    def _inicializar(self):
        """Inicialización perezosa de servicios."""
        # Servicios específicos
        self._pino_service = PinoService()
        self._olivo_service = OlivoService()
        self._lechuga_service = LechugaService()
        self._zanahoria_service = ZanahoriaService()
        
        # Registry de handlers por tipo
        from python_forestacion.entidades.cultivos.pino import Pino
        from python_forestacion.entidades.cultivos.olivo import Olivo
        from python_forestacion.entidades.cultivos.lechuga import Lechuga
        from python_forestacion.entidades.cultivos.zanahoria import Zanahoria
        
        self._handlers_absorcion = {
            Pino: self._absorber_pino,
            Olivo: self._absorber_olivo,
            Lechuga: self._absorber_lechuga,
            Zanahoria: self._absorber_zanahoria
        }
        
        self._handlers_mostrar = {
            Pino: self._mostrar_pino,
            Olivo: self._mostrar_olivo,
            Lechuga: self._mostrar_lechuga,
            Zanahoria: self._mostrar_zanahoria
        }
        
        self._handlers_crecer = {
            Pino: self._crecer_pino,
            Olivo: self._crecer_olivo
        }
    
    @classmethod
    def get_instance(cls):
        """
        Retorna instancia única del registry.
        
        Returns:
            Instancia única
        """
        return cls()
    
    def absorber_agua(self, cultivo: 'Cultivo') -> int:
        """
        Dispatch polimórfico para absorción.
        
        Args:
            cultivo: Cultivo que absorbe
            
        Returns:
            Litros absorbidos
            
        Raises:
            ValueError: Si tipo no registrado
        """
        tipo = type(cultivo)
        handler = self._handlers_absorcion.get(tipo)
        
        if handler is None:
            raise ValueError(f"Tipo no registrado: {tipo}")
        
        return handler(cultivo)
    
    def mostrar_datos(self, cultivo: 'Cultivo') -> None:
        """
        Dispatch polimórfico para mostrar datos.
        
        Args:
            cultivo: Cultivo a mostrar
            
        Raises:
            ValueError: Si tipo no registrado
        """
        tipo = type(cultivo)
        handler = self._handlers_mostrar.get(tipo)
        
        if handler is None:
            raise ValueError(f"Tipo no registrado: {tipo}")
        
        handler(cultivo)
    
    def crecer(self, cultivo: 'Cultivo') -> None:
        """
        Dispatch polimórfico para crecimiento (solo árboles).
        
        Args:
            cultivo: Cultivo a hacer crecer
        """
        tipo = type(cultivo)
        handler = self._handlers_crecer.get(tipo)
        
        if handler is not None:
            handler(cultivo)
    
    # Handlers privados
    def _absorber_pino(self, pino: 'Pino') -> int:
        return self._pino_service.absorver_agua(pino)
    
    def _absorber_olivo(self, olivo: 'Olivo') -> int:
        return self._olivo_service.absorver_agua(olivo)
    
    def _absorber_lechuga(self, lechuga: 'Lechuga') -> int:
        return self._lechuga_service.absorver_agua(lechuga)
    
    def _absorber_zanahoria(self, zanahoria: 'Zanahoria') -> int:
        return self._zanahoria_service.absorver_agua(zanahoria)
    
    def _mostrar_pino(self, pino: 'Pino') -> None:
        self._pino_service.mostrar_datos(pino)
    
    def _mostrar_olivo(self, olivo: 'Olivo') -> None:
        self._olivo_service.mostrar_datos(olivo)
    
    def _mostrar_lechuga(self, lechuga: 'Lechuga') -> None:
        self._lechuga_service.mostrar_datos(lechuga)
    
    def _mostrar_zanahoria(self, zanahoria: 'Zanahoria') -> None:
        self._zanahoria_service.mostrar_datos(zanahoria)
    
    def _crecer_pino(self, pino: 'Pino') -> None:
        self._pino_service.crecer(pino)
    
    def _crecer_olivo(self, olivo: 'Olivo') -> None:
        self._olivo_service.crecer(olivo)

# ==============================================================================
# ARCHIVO 57/69: lechuga_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/lechuga_service.py
# ==============================================================================

"""
Servicio para Lechuga.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_LECHUGA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.lechuga import Lechuga


class LechugaService(CultivoService):
    """
    Servicio específico para Lechuga.
    Usa estrategia constante.
    """
    
    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_LECHUGA))
    
    def mostrar_datos(self, lechuga: 'Lechuga') -> None:
        """
        Muestra datos específicos de la lechuga.
        
        Args:
            lechuga: Lechuga a mostrar
        """
        super().mostrar_datos(lechuga)
        print(f"Variedad: {lechuga.get_variedad()}")
        print(f"Invernadero: {lechuga.get_invernadero()}")

# ==============================================================================
# ARCHIVO 58/69: olivo_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/olivo_service.py
# ==============================================================================

"""
Servicio para Olivo.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_OLIVO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.olivo import Olivo


class OlivoService(ArbolService):
    """
    Servicio específico para Olivo.
    Usa estrategia seasonal.
    """
    
    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, olivo: 'Olivo') -> None:
        """
        Hace crecer el olivo.
        
        Args:
            olivo: Olivo a hacer crecer
        """
        altura_actual = olivo.get_altura()
        olivo.set_altura(altura_actual + CRECIMIENTO_OLIVO)
    
    def mostrar_datos(self, olivo: 'Olivo') -> None:
        """
        Muestra datos específicos del olivo.
        
        Args:
            olivo: Olivo a mostrar
        """
        super().mostrar_datos(olivo)
        print(f"Tipo aceituna: {olivo.get_tipo_aceituna().value}")

# ==============================================================================
# ARCHIVO 59/69: pino_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/pino_service.py
# ==============================================================================

"""
Servicio para Pino.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.arbol_service import ArbolService
from python_forestacion.patrones.strategy.impl.absorcion_seasonal_strategy import AbsorcionSeasonalStrategy
from python_forestacion.constantes import CRECIMIENTO_PINO

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.pino import Pino


class PinoService(ArbolService):
    """
    Servicio específico para Pino.
    Usa estrategia seasonal.
    """
    
    def __init__(self):
        """Inicializa con estrategia seasonal."""
        super().__init__(AbsorcionSeasonalStrategy())
    
    def crecer(self, pino: 'Pino') -> None:
        """
        Hace crecer el pino.
        
        Args:
            pino: Pino a hacer crecer
        """
        altura_actual = pino.get_altura()
        pino.set_altura(altura_actual + CRECIMIENTO_PINO)
    
    def mostrar_datos(self, pino: 'Pino') -> None:
        """
        Muestra datos específicos del pino.
        
        Args:
            pino: Pino a mostrar
        """
        super().mostrar_datos(pino)
        print(f"Variedad: {pino.get_variedad()}")

# ==============================================================================
# ARCHIVO 60/69: zanahoria_service.py
# Directorio: python_forestacion/servicios/cultivos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/cultivos/zanahoria_service.py
# ==============================================================================

"""
Servicio para Zanahoria.
"""

from typing import TYPE_CHECKING

from python_forestacion.servicios.cultivos.cultivo_service import CultivoService
from python_forestacion.patrones.strategy.impl.absorcion_constante_strategy import AbsorcionConstanteStrategy
from python_forestacion.constantes import ABSORCION_ZANAHORIA

if TYPE_CHECKING:
    from python_forestacion.entidades.cultivos.zanahoria import Zanahoria


class ZanahoriaService(CultivoService):
    """
    Servicio específico para Zanahoria.
    Usa estrategia constante.
    """
    
    def __init__(self):
        """Inicializa con estrategia constante."""
        super().__init__(AbsorcionConstanteStrategy(ABSORCION_ZANAHORIA))
    
    def mostrar_datos(self, zanahoria: 'Zanahoria') -> None:
        """
        Muestra datos específicos de la zanahoria.
        
        Args:
            zanahoria: Zanahoria a mostrar
        """
        super().mostrar_datos(zanahoria)
        print(f"Baby carrot: {zanahoria.get_es_baby()}")
        print(f"Invernadero: {zanahoria.get_invernadero()}")


################################################################################
# DIRECTORIO: python_forestacion/servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 61/69: __init__.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio/__init__.py
# ==============================================================================

"""
Servicios de alto nivel de negocio.
"""

# ==============================================================================
# ARCHIVO 62/69: fincas_service.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio/fincas_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 63/69: paquete.py
# Directorio: python_forestacion/servicios/negocio
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/negocio/paquete.py
# ==============================================================================

"""
Paquete genérico tipo-seguro para empaquetado.
"""

from typing import Generic, TypeVar, List

T = TypeVar('T')


class Paquete(Generic[T]):
    """
    Contenedor genérico tipo-seguro.
    
    Type Parameters:
        T: Tipo de elementos contenidos
    """
    
    def __init__(self):
        """Inicializa paquete vacío."""
        self._items: List[T] = []
    
    def agregar(self, item: T) -> None:
        """
        Agrega un item al paquete.
        
        Args:
            item: Item a agregar
        """
        self._items.append(item)
    
    def obtener_todos(self) -> List[T]:
        """
        Retorna todos los items (copia defensiva).
        
        Returns:
            Lista de items
        """
        return self._items.copy()
    
    def cantidad(self) -> int:
        """
        Retorna cantidad de items.
        
        Returns:
            Número de items
        """
        return len(self._items)


################################################################################
# DIRECTORIO: python_forestacion/servicios/personal
################################################################################

# ==============================================================================
# ARCHIVO 64/69: __init__.py
# Directorio: python_forestacion/servicios/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/personal/__init__.py
# ==============================================================================

"""
Servicios de gestión de personal.
"""

# ==============================================================================
# ARCHIVO 65/69: trabajador_service.py
# Directorio: python_forestacion/servicios/personal
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/personal/trabajador_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_forestacion/servicios/terrenos
################################################################################

# ==============================================================================
# ARCHIVO 66/69: __init__.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 67/69: plantacion_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/plantacion_service.py
# ==============================================================================

"""
Servicio para gestión de plantaciones.
"""

from typing import TYPE_CHECKING

from python_forestacion.patrones.factory.cultivo_factory import CultivoFactory
from python_forestacion.servicios.cultivos.cultivo_service_registry import CultivoServiceRegistry
from python_forestacion.excepciones.superficie_insuficiente_exception import SuperficieInsuficienteException
from python_forestacion.excepciones.agua_agotada_exception import AguaAgotadaException

if TYPE_CHECKING:
    from python_forestacion.entidades.terrenos.plantacion import Plantacion


class PlantacionService:
    """
    Servicio para operaciones sobre plantaciones.
    """
    
    def __init__(self):
        """Inicializa con registry de servicios."""
        self._registry = CultivoServiceRegistry.get_instance()
    
    def plantar(
        self,
        plantacion: 'Plantacion',
        especie: str,
        cantidad: int
    ) -> None:
        """
        Planta cultivos usando Factory Method.
        
        Args:
            plantacion: Plantación donde plantar
            especie: Especie a plantar
            cantidad: Cantidad a plantar
            
        Raises:
            SuperficieInsuficienteException: Si no hay superficie
        """
        # Crear uno para calcular superficie requerida
        cultivo_muestra = CultivoFactory.crear_cultivo(especie)
        superficie_requerida = cultivo_muestra.get_superficie() * cantidad
        superficie_disponible = plantacion.get_superficie_disponible()
        
        if superficie_requerida > superficie_disponible:
            raise SuperficieInsuficienteException(
                superficie_requerida,
                superficie_disponible
            )
        
        # Plantar
        for _ in range(cantidad):
            cultivo = CultivoFactory.crear_cultivo(especie)
            plantacion.agregar_cultivo(cultivo)
        
        # Actualizar superficie
        nueva_superficie = superficie_disponible - superficie_requerida
        plantacion.set_superficie_disponible(nueva_superficie)
    
    def regar(self, plantacion: 'Plantacion') -> None:
        """
        Riega todos los cultivos de la plantación.
        
        Args:
            plantacion: Plantación a regar
            
        Raises:
            AguaAgotadaException: Si no hay agua suficiente
        """
        cultivos = plantacion.get_cultivos()
        agua_disponible = plantacion.get_agua_disponible()
        
        # Calcular agua total necesaria
        agua_necesaria = 0
        for cultivo in cultivos:
            agua_necesaria += 5  # Estimación conservadora
        
        if agua_necesaria > agua_disponible:
            raise AguaAgotadaException(agua_necesaria, agua_disponible)
        
        # Regar cada cultivo
        for cultivo in cultivos:
            cantidad = self._registry.absorber_agua(cultivo)
            agua_disponible -= cantidad
            
            # Hacer crecer si es árbol
            self._registry.crecer(cultivo)
        
        plantacion.set_agua_disponible(agua_disponible)
    
    def cosechar(self, plantacion: 'Plantacion') -> None:
        """
        Cosecha los cultivos de la plantación.
        
        Args:
            plantacion: Plantación a cosechar
        """
        cultivos = plantacion.get_cultivos()
        print(f"[INFO] Cosechando {len(cultivos)} cultivos...")
    
    def fumigar(self, plantacion: 'Plantacion', plaguicida: str) -> None:
        """
        Aplica fumigación a la plantación.
        
        Args:
            plantacion: Plantación a fumigar
            plaguicida: Tipo de plaguicida
        """
        print(f"[INFO] Aplicando {plaguicida} a plantacion...")

# ==============================================================================
# ARCHIVO 68/69: registro_forestal_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/registro_forestal_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 69/69: tierra_service.py
# Directorio: python_forestacion/servicios/terrenos
# Ruta completa: /home/parra1/diseno/forestal/python_forestacion/servicios/terrenos/tierra_service.py
# ==============================================================================

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


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 69
# Generado: 2025-10-22 02:06:45
################################################################################
