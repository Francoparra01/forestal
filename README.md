# 🌲 Sistema de Gestión Forestal

![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Code Style](https://img.shields.io/badge/code%20style-PEP%208-orange)

**Sistema integral de gestión forestal y agrícola que implementa patrones de diseño de software con enfoque educativo y profesional.**

---

## 📋 Contenido

- [Descripción](#descripción)
- [Características](#características)
- [Patrones Implementados](#patrones-implementados)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura](#estructura)
- [Documentación](#documentación)
- [Licencia](#licencia)

---

## 🌍 Descripción

Sistema desarrollado en Python puro (sin dependencias externas) que aborda la gestión moderna de explotaciones forestales y agrícolas mediante la implementación de múltiples patrones de diseño.

### Problema que Resuelve

- **Gestión de múltiples tipos de cultivos** con requerimientos específicos
- **Monitoreo ambiental en tiempo real** con sensores automatizados
- **Control de personal** con certificaciones médicas
- **Optimización territorial** con registros catastrales
- **Trazabilidad completa** mediante persistencia de datos

---

## ⭐ Características

### 1. Gestión de Cultivos
- ✅ 4 tipos de cultivos (Pino, Olivo, Lechuga, Zanahoria)
- ✅ Creación dinámica mediante **Factory Method**
- ✅ Absorción diferenciada mediante **Strategy Pattern**
- ✅ Crecimiento automático para árboles

### 2. Sistema de Riego Inteligente
- ✅ Sensores de temperatura y humedad (**Observer Pattern**)
- ✅ Riego automatizado condicional
- ✅ Threading con graceful shutdown
- ✅ Notificaciones en tiempo real

### 3. Gestión de Personal
- ✅ Verificación de apto médico obligatorio
- ✅ Asignación y ejecución de tareas
- ✅ Herramientas certificadas H&S

### 4. Administración Territorial
- ✅ Registro catastral de tierras
- ✅ Control de superficie disponible
- ✅ Valuación de propiedades

### 5. Persistencia de Datos
- ✅ Serialización con Pickle
- ✅ Recuperación de registros históricos
- ✅ Manejo robusto de excepciones

---

## 🎯 Patrones Implementados

### 1. SINGLETON Pattern
- **Ubicación**: `cultivo_service_registry.py`
- **Propósito**: Instancia única del registro de servicios
- **Implementación**: Thread-safe con double-checked locking

### 2. FACTORY METHOD Pattern
- **Ubicación**: `cultivo_factory.py`
- **Propósito**: Creación de cultivos sin conocer clases concretas
- **Implementación**: Diccionario de factories

### 3. OBSERVER Pattern
- **Ubicación**: `patrones/observer/`
- **Propósito**: Notificaciones automáticas de eventos
- **Implementación**: Genéricos tipo-seguros con TypeVar

### 4. STRATEGY Pattern
- **Ubicación**: `patrones/strategy/`
- **Propósito**: Algoritmos intercambiables de absorción
- **Implementación**: Inyección por constructor

### 5. REGISTRY Pattern
- **Ubicación**: `cultivo_service_registry.py`
- **Propósito**: Dispatch polimórfico sin isinstance
- **Implementación**: Diccionario de handlers por tipo

---

## 💻 Requisitos

### Software
- Python 3.13 o superior
- Sistema operativo: Windows / Linux / macOS
- **Sin dependencias externas** (solo biblioteca estándar)

### Hardware
- RAM: 512 MB mínimo
- Disco: 50 MB libres
- Procesador: 1 GHz o superior

---

## 🚀 Instalación

### 1. Clonar repositorio
```bash
git clone https://github.com/usuario/python-forestal.git
cd python-forestal
```

### 2. Crear entorno virtual

**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Verificar instalación
```bash
python --version
# Debe mostrar Python 3.13 o superior
```

### 4. Ejecutar sistema
```bash
python main.py
```

---

## 📖 Uso

### Ejemplo Básico
```python
from python_forestacion.servicios.terrenos.tierra_service import TierraService
from python_forestacion.servicios.terrenos.plantacion_service import PlantacionService

# Crear terreno con plantación
tierra_service = TierraService()
terreno = tierra_service.crear_tierra_con_plantacion(
    id_padron_catastral=1,
    superficie=10000.0,
    domicilio="Mendoza, Argentina",
    nombre_plantacion="Finca Los Andes"
)

plantacion = terreno.get_finca()

# Plantar cultivos (usa Factory Method)
plantacion_service = PlantacionService()
plantacion_service.plantar(plantacion, "Pino", 5)
plantacion_service.plantar(plantacion, "Olivo", 3)

# Regar (usa Strategy Pattern)
plantacion_service.regar(plantacion)
```

### Sistema Automatizado
```python
from python_forestacion.riego.sensores.temperatura_reader_task import TemperaturaReaderTask
from python_forestacion.riego.sensores.humedad_reader_task import HumedadReaderTask
from python_forestacion.riego.control.control_riego_task import ControlRiegoTask

# Crear sensores
sensor_temp = TemperaturaReaderTask()
sensor_hum = HumedadReaderTask()

# Crear controlador
controlador = ControlRiegoTask(sensor_temp, sensor_hum, plantacion, plantacion_service)

# Iniciar sistema
sensor_temp.start()
sensor_hum.start()
controlador.start()

# Sistema funciona automáticamente...
```

---

## 📁 Estructura