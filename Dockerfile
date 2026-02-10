FROM apache/airflow:2.9.2

ARG CONSTRAINTS_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.12.txt"

RUN pip install --no-cache-dir --constraint "${CONSTRAINTS_URL}" \
    apache-airflow-providers-amazon \
    apache-airflow-providers-postgres \
    pandas \
    sqlalchemy \
    psycopg2-binary \
    pyarrow
