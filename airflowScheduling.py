from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_scraper():
    subprocess.run(['python', 'path/to/car_prices_selenium.py'])

with DAG('car_scraper', default_args=default_args, schedule_interval='@daily') as dag:
    scrape_task = PythonOperator(
        task_id='scrape_car_prices',
        python_callable=run_scraper
    )