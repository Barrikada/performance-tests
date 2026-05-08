# Performance Tests

This repository contains a performance testing framework for the
[Performance QA Engineer Course stand](https://github.com/Nikita-Filonov/performance-qa-engineer-course).
The stand includes banking domain services and infrastructure components such as `Kafka`, `Redis`, `PostgreSQL`,
`MinIO`, `Grafana`, and `Prometheus`, with APIs exposed via both **HTTP** and **gRPC**.

The framework is built with:

- `Python`
- `Locust`
- `Pydantic`
- `HTTPX`
- `grpcio`
- `Docker`

---

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Running Performance Tests](#running-performance-tests)
- [Monitoring \& Reports](#monitoring--reports)
- [CI/CD](#cicd)

---

## Project Overview

This project provides reusable load testing components for both protocols:

- **Scenarios** in `scenarios/http/` and `scenarios/grpc/`
- **Reusable API clients** in `clients/http/` and `clients/grpc/`
- **Seeding and test data generation** in `seeds/`
- **Shared tools and configuration** in `tools/` and `config.py`

Implemented scenarios include business flows for:

- Existing user: documents, operations, virtual card, purchase
- New user: accounts, documents, physical card, top up

---

## Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/Barrikada/performance-tests.git
cd performance-tests
```

### 2) Create a virtual environment

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running Performance Tests

Run a scenario using its Locust config:

```bash
locust --config=./scenarios/http/gateway/existing_user_get_documents/v1.0.conf
```

For gRPC scenarios:

```bash
locust --config=./scenarios/grpc/gateway/existing_user_get_documents/v1.0.conf
```

Generated HTML report is saved in the scenario directory, e.g.:

`./scenarios/http/gateway/existing_user_get_documents/report.html`

---

## Monitoring & Reports

- **Locust HTML reports**: generated in each scenario folder
- **Grafana**: http://localhost:3002
- **Prometheus**: http://localhost:9090
- **Load Testing Hub Panel**: http://localhost:13100
- **Load Testing Hub API docs**: http://localhost:13000/docs

---

## CI/CD

GitHub Actions workflow is configured in:

`./.github/workflows/performance-tests.yml`

It allows running scenarios in headless mode and publishing reports to GitHub Pages.
