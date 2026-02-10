from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

from airflow import DAG
from airflow.operators.python import PythonOperator

CSV_PATH = "/opt/airflow/data/your_dataset.csv"   # <-- change filename
PG_CONN = "postgresql+psycopg2://airflow:airflow@postgres:5432/etl_practice"

RAW_TABLE = "raw.your_dataset_raw"

def extract_transform_load():
    df = pd.read_csv(CSV_PATH)

    # tiny transform examples (customize)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    df["load_dts"] = pd.Timestamp.utcnow()

    engine = create_engine(PG_CONN)
    with engine.begin() as conn:
        df.to_sql(
            name=RAW_TABLE.split(".")[1],
            schema=RAW_TABLE.split(".")[0],
            con=conn,
            if_exists="replace",
            index=False
        )

with DAG(
    dag_id="csv_to_postgres_etl",
    start_date=datetime(2024, 1, 1),
    schedule=None,   # manual trigger
    catchup=False,
) as dag:
    run_etl = PythonOperator(
        task_id="extract_transform_load",
        python_callable=extract_transform_load
    )
