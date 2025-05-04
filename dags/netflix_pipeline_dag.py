from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta 
default_args = {
    'owner': 'abdo_mamdouh',
    'start_date': days_ago(1),
    'retries': 1,
    'retry_delay': timedelta(minutes = 5),
}

dag = DAG(
    default_args= default_args
    dag_id='netflix_analysis_dag',
    schedule_interval= None,
    catchup=False
)
spark_job = SparkSubmitOperator(
    task_id="run_netflix_spark_job",
    application="/opt/spark/apps/netflix_analysis_workflow.py",  # Mount this path properly
    conn_id="spark_default",
    verbose=True,
    # jars="/path/to/any/required/jars",
    driver_memory="1G",
    executor_memory="1G",
    dag= dag
)