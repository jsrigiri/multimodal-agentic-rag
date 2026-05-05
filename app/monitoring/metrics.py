import time


metrics = {
    "total_requests": 0,
    "route_counts": {
        "rag": 0,
        "csv": 0,
        "calculator": 0,
    },
    "latency_ms": [],
}


def record_request(route: str, latency_ms: float):
    metrics["total_requests"] += 1

    if route in metrics["route_counts"]:
        metrics["route_counts"][route] += 1

    metrics["latency_ms"].append(latency_ms)


def get_metrics():
    avg_latency = (
        sum(metrics["latency_ms"]) / len(metrics["latency_ms"])
        if metrics["latency_ms"]
        else 0
    )

    return {
        "total_requests": metrics["total_requests"],
        "route_counts": metrics["route_counts"],
        "avg_latency_ms": round(avg_latency, 2),
    }