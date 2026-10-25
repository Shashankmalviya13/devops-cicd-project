
from datetime import datetime
from pathlib import Path
import json

import psutil
from fastapi import FastAPI, Request
from fastapi.responses import Response
from prometheus_client import (
    Counter,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
)

from app.anomaly import detect_anomaly
from app.incident import create_incident, generate_alert


app = FastAPI(
    title="AIOps Monitoring Platform",
    description="AI-powered monitoring and incident response",
    version="1.0.0",
)

cpu_gauge = Gauge(
    "aiops_cpu_percent",
    "CPU usage percentage",
)

memory_gauge = Gauge(
    "aiops_memory_percent",
    "Memory usage percentage",
)

requests_counter = Counter(
    "aiops_http_requests_total",
    "Total HTTP requests received",
)

aiops_anomaly_detected = Gauge(
    "aiops_anomaly_detected",
    "1 if an anomaly is detected, otherwise 0",
)

aiops_anomaly_score = Gauge(
    "aiops_anomaly_score",
    "Isolation Forest anomaly decision score",
)


@app.middleware("http")
async def count_requests(request: Request, call_next):
    if request.url.path != "/prometheus":
        requests_counter.inc()

    response = await call_next(request)
    return response


@app.get("/")
def home():
    return {
        "message": "AIOps Platform is running!",
        "timestamp": datetime.now().isoformat(),
        "status": "success",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "aiops-monitor",
    }


@app.get("/metrics")
def metrics():
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)

    cpu_gauge.set(cpu)
    memory_gauge.set(memory.percent)

    return {
        "cpu_percent": cpu,
        "memory_percent": memory.percent,
        "memory_available_mb": round(
            memory.available / (1024 * 1024), 2
        ),
        "timestamp": datetime.now().isoformat(),
    }


@app.get("/anomaly")
def anomaly():
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=1)

    result = detect_anomaly(
        cpu_percent=cpu,
        memory_percent=memory.percent,
    )

    aiops_anomaly_detected.set(
        1 if result["is_anomaly"] else 0
    )
    aiops_anomaly_score.set(result["anomaly_score"])
    cpu_gauge.set(cpu)
    memory_gauge.set(memory.percent)

    incident_result = create_incident(result)
    alert_result = generate_alert(incident_result)

    return {
        **result,
        "incident": incident_result,
        "alert": alert_result,
    }


@app.get("/incidents")
def get_incidents():
    incident_file = Path("/app/data/incidents.json")

    if not incident_file.exists():
        return {
            "total": 0,
            "incidents": [],
        }

    incidents = []

    with incident_file.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                incidents.append(json.loads(line))

    return {
        "total": len(incidents),
        "incidents": incidents,
    }


@app.get("/prometheus")
def prometheus_metrics():
    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0.1)

    cpu_gauge.set(cpu)
    memory_gauge.set(memory.percent)

    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )

