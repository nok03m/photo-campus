# 📸 Photo Campus
Photo Campus es una solucion que permite el registro, modificacion y consultas de servicios fotograficos.

## ⚙️ Configuración y Uso
Sigue estos pasos para poner en marcha el entorno de desarrollo:

### 1. Requisitos Previos
Python 3.10+

### 2. Instalación
Clone el repositorio y configure el entorno virtual:

```
    git clone https://github.com/nok03m/photo-campus.git
    cd photo-campus
```

### 3. Ejecución
Para iniciar el servicio principal o el script de procesamiento:

```
    python main.py
```

## 📂 Estructura del Repositorio
El proyecto posee la siguiente estructura:
```
photo-campus/
├── data/               # Almacenamiento de los archivos .json
├── main.py             # Archivo principal para iniciar el programa
├── config.py           # Configuracion de las rutas absolutas
├── service.py          # Logica que realiza operaciones con los servicios (servicios.json)
└── README.md           # Documentación principal
```

## 🔄 Flujo de Trabajo (Workflow)
Para mantener un historial de git limpio y colaborativo, se emplea una metodología basada en Feature Branching:

- **Main Branch**: Contiene exclusivamente código estable y listo para producción.
- **Develop Branch**: Rama principal de integración para nuevas funcionalidades.
- **Feature Branches**: Cada nueva característica se desarrolla en una rama independiente (feature/nombre-de-la-mejora).
- **Pull Requests**: Todo cambio debe ser revisado mediante un PR antes de integrarse a develop.

## Documentacion de conflicto (Workflow)
En el repositorio local (al dia), se cambia a la **Develop Branch** para corregir las salidas del menu del programa(main.py), se registra en el historial de confirmaciones y se pasa a **Main Branch**
Se corrige las salidas desde esa rama (main.py) y tambien se registra en el historial de confirmaciones.

Al intentar hacer merge(develop a main), arroja un conflicto (no sabe cual cambio del mismo archivo entre los commits de las diferentes ramas conservar).

Se opta por resolverse 'Incoming' (Los de Develop eran mas apropiados para el caso) y se completa el Merge.

Posteriormente, se actualiza el repositorio remoto con Git Push
