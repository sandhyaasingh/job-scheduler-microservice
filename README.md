# 🛠️ Job Scheduler Microservice

A production-ready job scheduler microservice built with **FastAPI**, allowing users to create, list, and manage scheduled jobs via REST API. Jobs are scheduled using flexible **cron expressions** and executed by a background scheduler.

---

## 🚀 Features

- ✅ **Create Jobs** with custom name, description, and schedule
- ✅ **Cron-based Scheduling** using APScheduler
- ✅ **List All Jobs**
- ✅ **Get Job by ID**
- ✅ **Database-backed** (SQLite)
- ✅ **Swagger API Docs** (FastAPI auto-docs)
- ✅ **Modular code** following SOLID principles
- ✅ Designed for **Scalability & Performance**

---

## 🧪 API Endpoints

| Method | Endpoint        | Description                  |
|--------|------------------|------------------------------|
| `POST` | `/jobs`          | Create and schedule a new job |
| `GET`  | `/jobs`          | List all scheduled jobs       |
| `GET`  | `/jobs/{id}`     | Get details of a specific job |

---

## 📦 Technologies Used

- FastAPI
- SQLAlchemy
- APScheduler
- SQLite / PostgreSQL
- Pydantic
- Uvicorn

---

## 🖥️ Running Locally

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/scheduler-service.git
cd scheduler-service
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
uvicorn app.main:app --reload
```

### 5. Open API Docs
Go to 👉 http://127.0.0.1:8000/docs

---

## ⚙️ Example Job Payload

```bash
json

{
  "name": "Weekly Report Job",
  "description": "Sends report every Monday",
  "schedule_type": "cron",
  "cron_expression": "0 9 * * MON"
}
```
---

## 🌍 Scalability Strategy

To scale this job scheduler for high throughput (~10,000 users, ~1,000 services, and ~6,000 API requests per minute), we recommend:

### ✅ Horizontal Scaling
- **Stateless API Layer**: Run multiple FastAPI instances behind a load balancer (e.g., Kubernetes + NGINX or AWS ALB).
- **Containerization**: Use Docker and orchestrate with Kubernetes for global deployment.

### ✅ Background Processing
- **Job Workers**: Offload execution to Celery or RQ workers using Redis or RabbitMQ.
- **Task Queues**: Handle spikes, retries, and scheduled tasks cleanly with distributed queues.

### ✅ Distributed Scheduling
- **APScheduler with RedisJobStore**: Coordinate jobs across instances without duplication.
- **Centralized Scheduler**: Use a master-worker model to avoid conflicts in job execution.

### ✅ Database & Performance
- **Production Database**: Switch from SQLite to PostgreSQL or Redis.
- **Optimized Queries**: Index job IDs and `next_run` fields for faster lookups.
- **Async Support**: Use `async SQLAlchemy` or `databases` library for non-blocking DB access.

### ✅ API Management & Monitoring
- **API Gateway**: Protect and manage traffic with Kong or Traefik.
- **Monitoring**: Track metrics using Prometheus & Grafana for job status and system health.

---

