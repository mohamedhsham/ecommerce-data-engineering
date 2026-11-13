# E-Commerce Sales Data Engineering Project

## Project Overview

This project aims to build a data engineering pipeline for analyzing
e-commerce sales data using Python, PostgreSQL, Docker, and Kestra.

The pipeline will extract, clean, store, and process sales data
to support business analysis and visualization.

## Dataset

- Dataset: E-Commerce Sales
- File: ecommerce_sales_34500.csv
- Format: CSV
- Records: 34,500

## Analytical Questions

1. Which product categories generate the highest total sales revenue?
2. How do monthly sales revenues change over time?
3. Which product categories have the highest return rates?

## Proposed Architecture

CSV Dataset → Python Ingestion → PostgreSQL → Kestra → Dashboard

## Technologies

- Python: Data extraction and transformation
- PostgreSQL: Database storage
- Docker: Containerization
- pgAdmin: Database management
- Kestra: Workflow orchestration
- GitHub: Version control

## Project Structure

```text
ecommerce-data-engineering/
├── docs/
├── scripts/
├── sql/
├── flows/
├── docker-compose.yml
├── .env.example
├── .env  (i added that so that others know the credintals)
├── .gitignore
└── README.md
```

## Environment Setup

### 1. Clone the repository

git clone <repository-url>

### 2. Enter the project directory

cd ecommerce-data-engineering

### 3. Create the environment file

cp .env.example .env

Update the passwords inside `.env`.

### 4. Start the containers

docker compose up -d

### 5. Verify the containers

docker compose ps

### 6. Access pgAdmin

Open http://localhost:8080

Log in using the credentials configured in `.env`.

Register the PostgreSQL server using:

- Host: pgdatabase
- Port: 5432
- Database: ecommerce_db
- Username: ecommerce_user
- Password: Value configured in `.env`

## Current Progress

Phase 1:
- Dataset selected
- Analytical questions defined
- Architecture designed
- Docker environment configured
- PostgreSQL and pgAdmin connected

Future phases:
- Python ingestion
- Data cleaning and transformation
- Workflow orchestration
- Dashboard development
