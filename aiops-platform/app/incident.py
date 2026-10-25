from datetime import datetime, timezone
from pathlib import Path
import json
DATA_DIR = Path("/app/data")
DATA_DIR.mkdir(parents=True, exist_ok=True)
INCIDENT_FILE = DATA_DIR / "incidents.json"


def create_incident(anomaly_result):
    if not anomaly_result.get("is_anomaly", False):
        return {
            "created": False,
            "message": "No anomaly detected"
        }

    incident = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "severity": "WARNING",
        "status": "OPEN",
        "reason": "AI detected unusual CPU or memory usage",
        "details": anomaly_result
    }

    with INCIDENT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(incident) + "\n")

    return {
        "created": True,
        "incident": incident
    }
def generate_alert(incident_result):
    if not incident_result.get("created", False):
        return {
            "alert_sent": False,
            "message": "No new incident to alert"
        }

    incident = incident_result["incident"]

    alert_message = (
        f"AIOps ALERT: {incident['severity']} | "
        f"{incident['reason']} | "
        f"Time: {incident['timestamp']}"
    )

    print(alert_message)

    return {
        "alert_sent": True,
        "message": alert_message
    }