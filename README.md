
# neix

## Introducción

Este repositorio es un template con una arquitectura inicial para un proyecto en Python utilizando el framework **FastAPI**. El propósito de este proyecto es proporcionar una estructura básica para desarrollar aplicaciones que consumen APIs externas, procesando los datos con **Pandas** y realizando solicitudes HTTP con **httpx**.

### Herramientas principales utilizadas:

- **FastAPI**: Un framework web moderno y rápido para construir APIs con Python.
- **Pandas**: Utilizado para la manipulación y análisis de datos de manera eficiente.
- **httpx**: Un cliente HTTP asíncrono que permite realizar solicitudes HTTP a APIs externas de manera sencilla y eficiente.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- **Python**: Asegúrate de tener Python 3.6 o superior instalado en tu sistema.
- **pip**: El gestor de paquetes de Python, que generalmente se incluye con Python.

## Actualizar las dependencias

Para actualizar las dependencias del proyecto, utiliza el siguiente comando:

```bash
pip freeze > requirements.txt
```

## Crear y activar un entorno virtual

Para crear y activar un entorno virtual, ejecuta los siguientes comandos:

```bash
python -m venv myenv
.\myenv\Scripts\activate  # Para Windows
```

Para macOS/Linux, usa:

```bash
python3 -m venv myenv
source myenv/bin/activate  # Para macOS/Linux
```

## Instalar dependencias

Para instalar las dependencias listadas en el archivo `requirements.txt`, ejecuta:

```bash
pip install -r requirements.txt
```

## Ejecutar la aplicación

Para ejecutar tu aplicación, asegúrate de estar en el directorio raíz de tu proyecto y usa el siguiente comando:

```bash
uvicorn app.main:app --reload
```
