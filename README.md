# 🚀 AIOps Monitoring & Anomaly Detection Platform

An AI-powered monitoring platform that detects unusual system resource usage, creates incidents, monitors application metrics, and sends real-time Telegram alerts.

## 📌 Project Overview

This project combines Artificial Intelligence, DevOps, containerization, monitoring, and CI automation to build a practical AIOps solution.

The platform uses a machine learning model to identify anomalous CPU and memory usage. When an anomaly is detected, the application can create an incident and send an alert to a configured Telegram chat.

## ✨ Features

- 🤖 **AI-Based Anomaly Detection** — Uses Isolation Forest to identify unusual resource usage.
- 📊 **Prometheus Monitoring** — Collects application metrics.
- 📈 **Grafana Dashboards** — Visualizes monitoring metrics.
- 🚨 **Telegram Alerts** — Sends notifications when an incident triggers an alert.
- 🐳 **Docker Containerization** — Runs the application and monitoring services in containers.
- ⚙️ **GitHub Actions CI** — Automates tests and Docker image builds.
- 🩺 **Health Monitoring** — Provides application health and metrics endpoints.
- 📝 **Incident Management** — Stores incident records in JSON format.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| FastAPI | REST API |
| Scikit-learn | Anomaly detection |
| Prometheus | Metrics collection |
| Grafana | Monitoring dashboards |
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Git & GitHub | Version control |
| GitHub Actions | CI automation |
| Telegram Bot API | Alert notifications |

## 🏗️ Architecture

```text
       Python Application
               |
        AI Anomaly Detection
               |
        Incident Management
               |
        Telegram Notifications

       Application Metrics
               |
           Prometheus
               |
            Grafana

      GitHub Repository
               |
        GitHub Actions
               |
       Tests + Docker Build
```

## 📂 Project Structure

```text
aiops-platform/
├── app/
│   ├── main.py
│   ├── anomaly.py
│   └── incident.py
├── data/
│   └── incidents.json
├── prometheus/
│   └── prometheus.yml
├── .github/
│   └── workflows/
│       └── ci.yml
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

*Note: The workflow file may be located in the parent Git repository rather than inside `aiops-platform`; adjust the structure to match your actual repository.*

## ⚡ Getting Started

### Prerequisites

- Docker Desktop
- Git
- A Telegram account and bot (optional, for notifications)

### 1. Clone the repository

```bash
git clone https://github.com/Shashankmalviya13/devops-cicd-project.git
cd devops-cicd-project/aiops-platform
```

### 2. Configure environment variables

Create a `.env` file in the `aiops-platform` directory:

```dotenv
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
```

Replace the placeholders with your own credentials. Never commit your real `.env` file or expose your bot token publicly.

### 3. Start the application

```bash
docker compose up -d --build
```

### 4. Check the running services

```bash
docker compose ps
```

### 5. Access the services

- **FastAPI documentation:** http://localhost:8000/docs
- **Application health:** http://localhost:8000/health
- **Application metrics:** http://localhost:8000/metrics
- **Prometheus:** http://localhost:9090
- **Grafana:** http://localhost:3000

Use your configured Grafana credentials to sign in.

## 🔍 How It Works

1. The application exposes monitoring and health endpoints.
2. The anomaly detection model evaluates resource usage.
3. When unusual activity is detected, the application can create an incident.
4. The incident workflow sends a Telegram notification when configured.
5. Prometheus collects application metrics.
6. Grafana visualizes the collected metrics.
7. GitHub Actions runs the configured CI checks and Docker build.

## 🧪 Testing

Run the application's configured tests using the command supported by your repository. For example, if `test_app.py` is in the repository root:

```bash
python -m unittest -v test_app.py
```

Check service status and application logs:

```bash
docker compose ps
docker compose logs aiops-api
```

## 🔐 Security

- Store credentials in `.env`.
- Add `.env` to `.gitignore`.
- Never commit Telegram bot tokens or other secrets.
- Rotate any token that has been exposed.
- Use appropriate authentication and access controls before exposing services publicly.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- AI/ML-based anomaly detection
- Python API development
- Docker and Docker Compose
- Prometheus metrics and Grafana visualization
- Telegram Bot API integration
- Automated testing and CI workflows
- Incident creation and monitoring

## 🚀 Future Improvements

- Kubernetes deployment
- Advanced anomaly detection models
- Persistent incident storage using a database
- Role-based authentication
- Alert severity levels and deduplication
- Cloud deployment and centralized logging

## 👨‍💻 Author

**Shashank**

Computer Science & Engineering | Cloud Computing | DevOps | AI/ML

GitHub: https://github.com/Shashankmalviya13

---

⭐ If you find this project useful, consider starring the repository.
