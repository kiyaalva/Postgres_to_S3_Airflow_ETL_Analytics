AWS End-to-End Data Pipeline (Docker + Airflow + S3 + Athena)

📌 Overview

This project implements an end-to-end data analytics pipeline on AWS using a modern lakehouse-style architecture.
Raw data is extracted from a PostgreSQL source, orchestrated using Dockerized Apache Airflow, stored in Amazon S3 using Silver and Gold layers, queried with Amazon Athena, and visualized through Amazon QuickSight dashboards.

The focus of this project is scalability, data quality, and production-ready orchestration.

Aws.png

🔄 Data Flow

PostgreSQL (Raw Source)

Acts as the system of record

Contains raw transactional data with minimal preprocessing

Apache Airflow (Dockerized)

Orchestrates all ETL workflows

Extracts data from Postgres

Applies validation and transformation logic

Manages retries, scheduling, and dependencies

Amazon S3 – Silver Layer

Cleaned and standardized datasets

Schema validation applied

Partitioned for efficient querying

Amazon S3 – Gold Layer

Business-ready curated datasets

Aggregations and analytics-friendly models

Optimized for Athena and BI consumption

Amazon Athena

Serverless SQL analytics on curated S3 data

Used for analytical queries and semantic views

Amazon QuickSight

Dashboards and visual analytics

Consumes Athena datasets for reporting

🐳 Why Docker?

Docker is used to containerize Airflow and its dependencies, ensuring:

Consistent runtime across local and AWS environments

Simplified dependency management

Reproducible and portable ETL execution

Easier scaling and deployment