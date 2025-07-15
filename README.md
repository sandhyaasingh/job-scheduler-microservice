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

## 🌍 Scaling Strategy (For Brownie Points 🌟)

To scale this microservice across ~10,000 users, ~1,000 services, and ~6,000 API requests/minute, we recommend:

### ✅ Horizontal Scalability
- Containerize with Docker and deploy multiple instances behind a load balancer (e.g., Kubernetes + NGINX or AWS ALB)
- Use Redis or a distributed store to coordinate scheduled jobs across instances (e.g., APScheduler + RedisJobStore)

### ✅ Background Processing
- Offload job execution to background workers (e.g., Celery + Redis/RabbitMQ)
- Use task queues to handle job spikes and retries gracefully

### ✅ Database & Performance
- Switch from SQLite to PostgreSQL for production
- Use indexes on job.id and next_run for efficient querying
- Add async support with `databases` or `async SQLAlchemy` for high I/O workloads

---

### 🔄 Scalability Strategy

To scale this job scheduler for high throughput (~10,000 users and ~6,000 API calls/minute):

- **Stateless API Layer**: FastAPI service can run in multiple instances behind a load balancer (e.g., Nginx).
- **Background Workers**: Use Celery/RQ for async job handling in production.
- **Distributed Job Store**: Use PostgreSQL or Redis for multi-instance support.
- **Job Queueing**: APScheduler + Redis for shared job queue across services.
- **Monitoring**: Use Prometheus & Grafana to monitor job runs.
- **API Gateway**: Protect APIs with rate-limiting & routing using Kong or Traefik.

---

