from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def preprocess_data():
    # Code for data preprocessing
    print("Data preprocessing completed")

def train_model():  
    # Code for model training
    print("Model training completed")

def evaluate_model():  
    # Code for model evaluation
    print("Model evaluation completed")
    
with DAG(
    'mlpipeline',
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:
    
    # define tasks
    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
    )

    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )

    # define dependencies(workflow)
    preprocess_task >> train_task >> evaluate_task