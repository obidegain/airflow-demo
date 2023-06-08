from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd

def consulta_api():
    for i in range(10):
        i+=1
    return i

def get_data_from_api():
    # Aquí va el código para consultar la API y obtener los datos
    data = consulta_api()  # Supongamos que esto devuelve los datos obtenidos
    task_instance = PythonOperator.get_current().ti
    task_instance.xcom_push(key='my_data', value=data)  # Almacena los datos en XCom

def process_data(data):
    # Aquí va el código para trabajar los datos obtenidos de la API
    # Puedes acceder a los datos a través de xcom_pull()
    data = task_instance.xcom_pull(key='my_data', task_ids='get_data')
    df = pd.DataFrame(columns=['Valores'])
    df['Valores'] = data
    df.to_excel('este_es_mi_primer_excel.xlsx')
    # Realiza las transformaciones o manipulaciones necesarias
    # Retorna los datos procesados

def store_data_in_database(data):
    # Aquí va el código para almacenar los datos en la base de datos
    # Puedes utilizar bibliotecas como SQLAlchemy o pymongo para interactuar con la base de datos
    # Realiza las operaciones necesarias para guardar los datos

default_args = {
    'start_date': datetime(2023, 6, 6),  # La fecha en que quieres que comience la ejecución
}

dag = DAG('my_pipeline', default_args=default_args, schedule_interval=None)

get_data_task = PythonOperator(
    task_id='get_data',
    python_callable=get_data_from_api,
    dag=dag
)

process_data_task = PythonOperator(
    task_id='process_data',
    python_callable=process_data,
    dag=dag
)

store_data_task = PythonOperator(
    task_id='store_data',
    python_callable=store_data_in_database,
    dag=dag
)

get_data_task >> process_data_task >> store_data_task
