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