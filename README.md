# Taxi-Company-Data-Analysis
SQL Queries, Data Visualization, and Statistical Tests

📊 Análisis de Datos de Viajes en Taxi de Chicago

![Image Alt](https://github.com/AeroGenCreator/Taxi-Company-Data-Analysis/blob/main/1.png)
[Link al Dashboard Interactivo]()

Esta presentación resume los pasos clave del Análisis Exploratorio de Datos (EDA) y la Prueba de Hipótesis realizada sobre los datos de viajes en taxi en Chicago.
Paso 1: 🔎 Análisis Exploratorio de Datos (EDA)

El objetivo de esta fase fue examinar los patrones de viajes utilizando dos datasets principales:

    project_sql_result_01.csv: Datos sobre el rendimiento de las compañías de taxi.

        Variables clave: company_name (Nombre de la compañía), trips_amount (Número de viajes el 15 y 16 de noviembre de 2017).

    project_sql_result_04.csv: Datos sobre las ubicaciones de finalización de los viajes.

        Variables clave: dropoff_location_name (Barrio de finalización), average_trips (Promedio diario de viajes finalizados en noviembre de 2017).

Tareas Clave y Resultados

    Preparación de Datos: Importación, estudio inicial de la estructura, y aseguramiento de la corrección de tipos de datos (por ejemplo, asegurando que las cantidades de viajes sean numéricas).

    Identificación de los 10 Principales Barrios: Se identificaron los 10 principales barrios de Chicago basándose en el promedio de finalizaciones de viaje (average_trips).

    Visualizaciones Clave:

        Gráfico de Barras: Empresas de Taxi vs. Número de Viajes

            Objetivo: Mostrar la cuota de mercado por volumen de viajes entre las distintas compañías.

            Conclusión Clave: Identificar las compañías dominantes en términos de volumen de viajes y la distribución de la actividad en el mercado de taxis.

        Gráfico de Pastel: Top 10 Barrios por Finalizaciones de Viaje

            Objetivo: Visualizar qué barrios son los principales destinos de los viajes en taxi.

            Conclusión Clave: Determinar las zonas de mayor demanda de llegada, lo que puede indicar centros de negocios, turismo o alta densidad residencial (ej. el Loop, Aeropuerto O'Hare).

Paso 2: 🧪 Prueba de Hipótesis

Esta fase se centró en probar cómo las condiciones meteorológicas afectan la duración del viaje entre dos puntos clave: Loop y el Aeropuerto Internacional O'Hare (ORD).

    Dataset utilizado: project_sql_result_07.csv.

        Variables clave: start_ts (Hora de recogida), weather_conditions (Lluvioso o No Lluvioso), duration_seconds (Duración del viaje).
