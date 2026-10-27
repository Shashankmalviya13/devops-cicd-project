
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import requests

DATA_DIR = Path("/app/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
INCIDENT_FILE = DATA_DIR / "incidents.json"

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def send_telegram_alert(message):
    """Send an alert to the configured Telegram chat."""

    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram alert skipped: credentials not configured.", flush=True)
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
            },
            timeout=10,
        )
        response.raise_for_status()
        result = response.json()

        if not result.get("ok"):
            print("Telegram API did not confirm the alert.", flush=True)
            return False

        print("Telegram alert sent successfully.", flush=True)
        return True

    except requests.RequestException as exc:
        print(f"Telegram alert failed: {exc}", flush=True)
        return False


def create_incident(anomaly_result):
    """Create and save an incident when an anomaly is detected."""

    if not anomaly_result.get("is_anomaly", False):
        return {
            "created": False,
            "message": "No anomaly detected",
        }

    incident = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "severity": "WARNING",
        "status": "OPEN",
        "reason": "AI detected unusual CPU or memory usage",
        "details": anomaly_result,
    }

    with INCIDENT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(incident) + "\n")

    return {
        "created": True,
        "incident": incident,
    }


def generate_alert(incident_result):
    """Send a Telegram notification for a newly created incident."""

    if not incident_result.get("created", False):
        return {
            "alert_sent": False,
            "message": "No new incident to alert",
        }

    incident = incident_result["incident"]
    details = incident["details"]

    alert_message = (
        "🚨 AIOps ALERT\n"
        f"Severity: {incident['severity']}\n"
        f"Status: {incident['status']}\n"
        f"Reason: {incident['reason']}\n"
        f"CPU: {details.get('cpu_percent', 'N/A')}%\n"
        f"Memory: {details.get('memory_percent', 'N/A')}%\n"
        f"Time: {incident['timestamp']}"
    )

    sent = send_telegram_alert(alert_message)

    return {
        "alert_sent": sent,
        "message": alert_message if sent else "Telegram alert could not be sent",
    }
