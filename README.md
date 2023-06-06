# airflow-demo

Creamos un entorno virtual:
```
python3 -m venv venv
```
Lo activamos
```
source venv/bin/activate
```

Instalamos apache airflow:
```
pip3 install apache-airflow
```

Inicializamos el proyecto y la base de datos:
```
airflow db init
```


Creamos un usuario:
```
airflow users create \                                
          --username admin \                                                                       
          --firstname Octavio \
          --lastname Bidegain \
          --role Admin \
          --email octa.bidegain@gmail.com
```
**La pass que setee es: password**

Si ya tenemos el pipeline creado, estamos en condiciones de ejecutar el scheduler y webserver:
**Muy importante: hay que tener la misma referencia a home desde las terminales:**


1) En la terminarl 1, ponemos la referencia de AIRFLOW_HOME y ejecutamos el scheduler:
```
export AIRFLOW_HOME=`pwd`/airflow
```
```
airflow scheduler
```

2) En la terminarl 2, ponemos la referencia de AIRFLOW_HOME y ejecutamos el webserver:
```
export AIRFLOW_HOME=`pwd`/airflow
```
```
airflow webserver --port 8080
```
