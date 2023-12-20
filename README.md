# SM_LAB

Proyecto de laboratorio para la asignatura sistemas multiagente

Daniel López Martínez
Miguel Torres Medina

# Introducción
En este documento se presenta el informe final del proyecto de Sistemas Multiagentes. Se incluyen todos los procesos realizados en Minería de Datos junto con las nuevas características añadidas.
 
# Selección, preprocesado y transformación
En la fase inicial del proyecto, analizamos los datos proporcionados por el reto de Cajamar Agroanalysis y definimos unas hipótesis relacionadas con el impacto de la pandemia en el consumo de frutas y hortalizas en España. Seleccionamos cinco conjuntos de datos relevantes que abarcaban información sobre el consumo en España, datos sobre las ventas de varios mercados, exportaciones e importaciones y la evolución mundial de la pandemia.
Las líneas de trabajo que definimos son las siguientes:
La pandemia afectó al consumo de frutas y hortalizas en España.
La pandemia afectó a las importaciones en España.
Las estaciones del año afectan al consumo de frutas y hortalizas en España.
Después llevamos a cabo el preprocesado y transformación de los datos. Seleccionamos los campos relevantes de cada conjunto de datos para evaluar cada hipótesis y llevamos a cabo la limpieza de datos, normalizando nombres de productos y ajustando formatos de fechas, entre otras cosas.
Por último, agrupamos todos los conjuntos de datos en uno solo, mostrando los campos ‘Producto’, ‘Año’, ’Mes’, ‘País’, ‘Casos’ y ‘Muertes’. Tras esto, empleamos varios procesos para evaluar cada una de nuestras hipótesis.
Para la primera hipótesis decidimos usar árboles de decisión y random forests, descartando la regresión lineal, ya que la distribución de los datos a estudiar no es interpretable linealmente. Tras la evaluación, llegamos a la conclusión de que la hipótesis se acepta, ya que hubo un cambio en el consumo per cápita durante la pandemia.
Para la segunda hipótesis decidimos usar una regresión lineal. Tras la evaluación, pudimos comprobar que sí hubo un cambio durante la pandemia respecto a las importaciones en España, ya que fueron en incremento.
Para la tercera hipótesis decidimos usar un clustering mediante dos técnicas diferentes: K-Means y DBSCAN. Tras la evaluación, llegamos a la conclusión de que con los datos que poseemos no hemos encontrado evidencias que sustenten la hipótesis.
Herramientas empleadas
Hemos elegido PostgreSQL como sistema de gestión de bases de datos y Python como lenguaje de programación. PostgreSQL utiliza una licencia de código abierto, es compatible con diversos estándares y altamente escalable. Además, dispone de muchas opciones de administración y monitorización que facilitan su gestión,  mantenimiento y seguridad, proporcionando funciones avanzadas de autenticación, autorización y cifrado de datos.
También hemos utilizado SQLalchemy, que permite escribir código Python para interactuar con la base de datos en lugar de usar lenguaje SQL. Además, permite la creación de consultas SQL dinámicamente mediante el uso de expresiones y constructores de consulta.
Ya que queríamos emplear la herramienta FastAPI para desarrollar la aplicación, debíamos utilizar Python como lenguaje de programación. Esto nos iba a simplificar en gran medida el trabajo, gracias a la automatización de la documentación, integración con sistemas de bases de datos y su soporte para el despliegue con Docker.
Por otra parte, Docker ofrece la posibilidad de encapsular la aplicación y sus dependencias en contenedores y desplegar la base de datos en otro contenedor, permitiendo una gestión independiente al resto de la aplicación. Utilizar contenedores Docker para PostgreSQL simplifica la administración de la base de datos y facilita el despliegue continuo de la aplicación desarrollada.

# Objetivos
El objetivo de este proyecto es desarrollar una aplicación de consultas a una base de datos mediante FastAPI y Docker. Queremos implementar tres funciones:
La primera función que queremos implementar es extraer los conjuntos de datos de sus respectivas páginas web, limpiarlos, procesarlos y unirlos en uno solo.
La segunda función que buscamos implementar es la capacidad de cargar conjuntos de datos en una base de datos que estará encapsulada dentro de un contenedor Docker. Esto proporcionará un entorno aislado y fácilmente reproducible, asegurando la consistencia y portabilidad de la aplicación.
La tercera función tiene como objetivo encapsular una aplicación de gestión de búsquedas sobre los conjuntos de datos almacenados. Esta aplicación permitirá a los usuarios realizar consultas y filtrar la información de manera eficiente, aprovechando las capacidades de FastAPI para manejar solicitudes web de manera rápida y sencilla. La separación de la base de datos en otro contenedor Docker garantiza una arquitectura modular y escalable, donde la gestión de datos y la interfaz de usuario se mantienen separadas para facilitar el mantenimiento y la escalabilidad del sistema.

# Implementación
El proyecto consta de tres módulos principales, cada uno cumpliendo una de las funciones mencionadas anteriormente:
El módulo extraction.py se encarga de extraer los conjuntos de datos desde las respectivas páginas web mediante “BeautifulSoup”, filtrando por los años que son relevantes para nuestras hipótesis. Una vez ha extraído los datos necesarios, los almacena localmente en la carpeta “data”. Este módulo también se encarga de gestionar la carga de los datasets a la base de datos y la creación de nuevas tablas si fuera necesario.
El módulo load.py se encarga de limpiar los conjuntos de datos, normalizar los nombres y formatos y unir todos los conjuntos de datos en un dataset final. Después, se cargan a la base de datos junto con los datos crudos.
El módulo serve.py se encarga de gestionar las consultas a la base de datos y devolver los resultados correspondientes. Para este módulo ha sido importante el uso de la herramienta sqlAlchemy, que ha ayudado a simplificar la tarea.
Los demás archivos de la aplicación tienen diversas funcionalidades. El módulo main.py inicializa la aplicación con FastAPI, el módulo config.py contiene la configuración de la base de datos (host, puerto, usuario, contraseña…); y, en caso de que falle, también hay un archivo database.ini con redundancia de la configuración.

# Resultado
Debido a varios errores encontrados durante la implementación, no hemos podido completar el proyecto. En este momento, hemos sido capaces de crear los contenedores de Docker para encapsular tanto la aplicación como la base de datos, e incluso cargar algunos conjuntos de datos a esta. Tenemos problemas de permisos que no hemos sido capaces de resolver.

Para levantar la aplicación se debe ejecutar el comando “docker-compose up –build -d” en el nivel más alto del directorio del proyecto. La aplicación se debería exponer en el puerto 80 (localhost:80).
