from flask import Flask, render_template
import requests
import json
import time

app = Flask(__name__)


@app.route("/")
def dashboard():

    servers = []
    alerts = []

    with open("servers.json") as file:
        targets = json.load(file)

    for server in targets:

        start = time.time()

        try:

            response = requests.get(
                f"http://{server['ip']}:5000/metrics",
                timeout=4
            )

            metrics = response.json()

            latency = round(
                (time.time() - start) * 1000,
                2
            )

            cpu = metrics["cpu_percent"]

            memory = metrics["memory"]["used_percent"]

            disk = metrics["disk"]["used_percent"]

            health_score = 100

            health_score -= cpu * 0.2
            health_score -= memory * 0.3
            health_score -= disk * 0.5

            health_score = max(
                0,
                round(health_score)
            )

            if cpu > 90:
                alerts.append(
                    f"{server['name']} CPU Critical"
                )

            if memory > 85:
                alerts.append(
                    f"{server['name']} Memory High"
                )

            if disk > 90:
                alerts.append(
                    f"{server['name']} Disk Critical"
                )

            servers.append({

                "name": server["name"],

                "status": "ONLINE",

                "latency": latency,

                "health_score": health_score,

                "metrics": metrics
            })

        except Exception as e:

            servers.append({

                "name": server["name"],

                "status": "OFFLINE",

                "latency": "N/A",

                "health_score": 0,

                "metrics": None,

                "error": str(e)
            })

    return render_template(
        "dashboard.html",
        servers=servers,
        alerts=alerts
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )