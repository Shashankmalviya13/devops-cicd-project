
import numpy as np
from sklearn.ensemble import IsolationForest

# Demo baseline: typical CPU and memory usage patterns.
# Replace this synthetic baseline with real historical metrics
# before using the model for production decisions.
rng = np.random.default_rng(42)

normal_data = np.column_stack([
    rng.uniform(5, 60, 1000),   # CPU usage %
    rng.uniform(20, 80, 1000),  # Memory usage %
])

# Train the Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42,
)

model.fit(normal_data)


def detect_anomaly(cpu_percent: float, memory_percent: float):
    """
    Predict whether CPU and memory usage look unusual.
    Returns the prediction, input metrics and anomaly score.
    """
    sample = np.array([[cpu_percent, memory_percent]])

    prediction = int(model.predict(sample)[0])
    score = float(model.decision_function(sample)[0])

    is_anomaly = prediction == -1

    return {
        "status": "anomaly" if is_anomaly else "normal",
        "is_anomaly": is_anomaly,
        "cpu_percent": round(cpu_percent, 2),
        "memory_percent": round(memory_percent, 2),
        "anomaly_score": round(score, 4),
        "model": "Isolation Forest",
    }
