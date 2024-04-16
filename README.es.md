## Predictor de Resultados de Partidos de la NBA

### Visión General
El proyecto "Predictor de Resultados de Partidos de la NBA" se centra en predecir el resultado de los partidos de baloncesto de la NBA utilizando diversas estadísticas de equipos e información específica del juego. El proyecto utiliza técnicas de aprendizaje automático, específicamente un clasificador de bosque aleatorio, para analizar datos históricos de partidos de la NBA y hacer predicciones sobre los resultados de juegos futuros. La aplicación proporciona una interfaz fácil de usar construida con Streamlit, que permite a los usuarios ingresar parámetros relacionados con el juego, como abreviaturas de equipos, enfrentamientos, fecha del juego y tipo de temporada. Una vez que se ingresan los datos, el modelo predice si el equipo local ganará o perderá el juego según la información proporcionada. El proyecto tiene como objetivo ayudar a los entusiastas de la NBA y a los analistas deportivos a hacer predicciones informadas sobre los resultados de los juegos.

### Estructura
El proyecto está organizado de la siguiente manera:

- **app.py:** El script principal de Python que ejecuta el proyecto y sirve como la interfaz de usuario.
- **total_data_final.csv:** Conjunto de datos que contiene datos de partidos de la NBA limpios y preprocesados.
- **new_random_forest_regressor.pkl:** Modelo de aprendizaje automático preentrenado para predecir resultados de partidos.
- **utils.py:** Funciones de utilidad para preprocesamiento de datos y carga de modelos.
- **requirements.txt:** Lista de paquetes de Python requeridos.

### Configuración
**Prerrequisitos:** Asegúrate de tener Python 3.11+ instalado en tu sistema. También necesitarás pip para instalar los paquetes de Python necesarios.

**Instalación:**

1. Clona el repositorio del proyecto en tu máquina local.
2. Navega hasta el directorio del proyecto e instala los paquetes de Python requeridos:

```bash
pip install -r requirements.txt
Ejecución de la Aplicación
Para ejecutar la aplicación, ejecuta el script app.py desde la raíz del directorio del proyecto:

bash
Copy code
streamlit run app.py
Trabajando con los Datos
El proyecto utiliza el archivo total_data_final.csv como conjunto de datos para entrenar el modelo de aprendizaje automático. Si necesitas preprocesar o analizar los datos más a fondo, puedes modificar el script app.py o crear scripts de Python adicionales para manejar estas tareas.

Colaboradores
Kevin Kenneth
Dario Zerpa

Notas
Este proyecto asume familiaridad básica con la programación en Python y los conceptos de aprendizaje automático.
Para cualquier problema o pregunta, por favor contacta.
