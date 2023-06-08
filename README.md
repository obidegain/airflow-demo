# airflow-demo

## Entorno virtual

Creamos un entorno virtual:
```
python3 -m venv venv
```
Lo activamos
```
source venv/bin/activate
```

## Instalar paquetes

Instalamos apache airflow:
```
pip3 install apache-airflow
```

## Trabajar en airflow

### Pasos iniciales

1) Inicializamos el proyecto y la base de datos:
```
airflow db init
```

2) Creamos un usuario:
```
airflow users create \                                
          --username admin \                                                                       
          --firstname Octavio \
          --lastname Bidegain \
          --role Admin \
          --email octa.bidegain@gmail.com
```
**La pass que setee es: password**

3) Si ya tenemos el pipeline creado, estamos en condiciones de ejecutar el scheduler y webserver:
**Muy importante: hay que tener la misma referencia a home desde las terminales:**

3.1) En la terminarl 1, ponemos la referencia de AIRFLOW_HOME y ejecutamos el scheduler:
```
export AIRFLOW_HOME=`pwd`/airflow
```
```
airflow scheduler
```

3.2) En la terminarl 2, ponemos la referencia de AIRFLOW_HOME y ejecutamos el webserver:
```
export AIRFLOW_HOME=`pwd`/airflow
```
```
airflow webserver --port 8080
```

3.3) SOLUCIÓN DEFINITIVA: Para tener que evitar explicitar la variable de entorno AIRFLOW_HOME cada vez que abro una terminal, puedo definirlo dentro del archivo activate del entorno virtual.
Navego hasta el archivo ubicado en venv/bin/activate y agrego **export AIRFLOW_HOME=`pwd`/airflow** en la última línea.

4) Si queremos evitar que se carguen todos los ejemplos, debemos editar el archivo **airflow.cfg**:
4.1) Busca la sección [core] en el archivo de configuración.
4.2) Dentro de la sección [core], busca la línea que comienza con load_examples y establece su valor en False. Si no encuentras esta línea, puedes agregarla manualmente con el valor load_examples = False.
4.3) Guarda los cambios en el archivo airflow.cfg.
4.4) Recuerda reiniciar el servidor web de Airflow después de modificar la configuración para que los cambios surtan efecto.

### DAGS

Otro punto importante es que hay que generar archivos con los pipelines. Estos archivos, para que se ejecuten, deben estar en la carpeta correspondiente.
¿Cuál es esa carpeta? Se encuentra especificada dentro del archivos **airflow.cfg** con el valor **dags_folder**. En mi caso, apuntaba a la carpeta principal que se llama airflow-demo/dags. Por lo tanto tuve que crear la carpeta dags dentro de airflow-demo.
