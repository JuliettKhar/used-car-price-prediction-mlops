# used-car-price-prediction-mlopsф# Used Car Price Prediction MLOps Pipeline

An end-to-end MLOps project for predicting used car prices in the Indian automotive market.

The project covers the complete machine learning lifecycle, including data preparation, experiment tracking, workflow orchestration, model deployment, monitoring, testing, and CI/CD.

## Problem Description

The objective of this project is to predict the market price of a used car based on vehicle characteristics such as brand, transmission type, fuel type, engine capacity, ownership history, and mileage.

This project was developed as the final project for the MLOps Zoomcamp program.

## Dataset

Dataset: Cars India – Pre-Owned Vehicles

Target variable:

* `price`

Features:

* brand
* model
* transmission
* fuel_type
* ownership
* spare_key
* reg_number
* car_age
* engine_capacity(CC)
* km_driven

Excluded features:

* `overall_cost` (potential target leakage)
* `reg_year`
* `has_insurance`
* `title`

## Project Architecture

```text
Raw Data
    │
    ▼
Data Cleaning
    │
    ▼
Feature Engineering
    │
    ▼
Model Training
(Random Forest)
    │
    ▼
MLflow Tracking
    │
    ▼
Model Registry
    │
    ▼
Docker Deployment
    │
    ▼
Monitoring (Evidently)
```

## Technologies

* Python
* Pandas
* Scikit-learn
* MLflow
* Prefect
* Docker
* Evidently
* Pytest
* Ruff
* Pre-commit
* GitHub Actions

## Experiment Tracking

MLflow is used to track:

* parameters
* metrics
* artifacts
* trained models

The project also uses the MLflow Model Registry to manage model versions.

## Workflow Orchestration

Prefect is used to orchestrate the training pipeline.

Pipeline steps:

1. Load data
2. Clean data
3. Train model
4. Log experiment
5. Register model

## Model Deployment

The prediction service is containerized using Docker.

Example:

```bash
docker build -t used-car-price-prediction .
docker run --rm used-car-price-prediction
```

Example output:

```text
Predicted price: 1116391
```

## Monitoring

Evidently is used for data drift monitoring.

Reference dataset:

* vehicles manufactured up to 2021

Current dataset:

* vehicles manufactured after 2021

The monitoring report detected dataset drift in multiple features, including:

* car_age
* km_driven
* brand
* model
* prediction distribution

This indicates that newer vehicles differ significantly from the training data and may require model retraining.

## Model Performance

Production model:

* RandomForestRegressor

Evaluation strategy:

* Time-based split

Training data:

* make_year <= 2021

Test data:

* make_year > 2021

Metrics:

* RMSE: ~230,000
* MAE: ~156,000
* R²: ~0.67

Leakage investigation:

Including the `overall_cost` feature increased model performance dramatically (R² ≈ 0.98). Further analysis revealed a very strong correlation between `overall_cost` and the target variable, suggesting potential target leakage. Therefore, this feature was excluded from the production model.

## Tests

Unit tests:

* data cleaning
* feature configuration

Integration tests:

* prediction pipeline
* Docker execution

Run tests:

```bash
pytest tests/
```

## Best Practices

Implemented:

* Unit tests
* Integration tests
* Makefile
* Ruff
* Pre-commit hooks
* GitHub Actions CI

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Train model:

```bash
make train
```

Run tests:

```bash
make test
```

Generate monitoring report:

```bash
make monitor
```

Run training pipeline:

```bash
make pipeline
```

Run prediction:

```bash
make predict
```

Build Docker image:

```bash
make docker-build
```

Run Docker container:

```bash
make docker-run
```
