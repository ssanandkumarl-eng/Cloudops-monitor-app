from flask import Flask, render_template, request, redirect
import requests
import json
import os
import time

app = Flask(__name__)

SERVERS_FILE = "servers.json"


def load_servers():

    if not os.path.exists(SERVERS_FILE):

        with open(SERVERS_FILE, "w") as f:
            json.dump([], f)

    with open(SERVERS_FILE, "r") as f:
        return json.load(f)


def save_servers(data):

    with open(SERVERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


@app.route("/", methods=["GET", "POST"])
def monitor():

    if request.method == "POST":

        ip = request.form.get("ip")

        servers = load_servers()

        already_exists = False

        for s in servers:

            if s["ip"] == ip:

                already_exists = True

        if not already_exists:

            servers.append({

                "name": f"AWS-{ip}",

                "ip": ip

            })

            save_servers(servers)

        return redirect("/")

    monitored = []

    servers = load_servers()

    for server in servers:

        start = time.time()

        try:

            response = requests.get(
                f"http://{server['ip']}:5000/metrics",
                timeout=5
            )

            latency = round(
                (time.time() - start) * 1000,
                2
            )

            metrics = response.json()

            monitored.append({

                "name": server["name"],

                "ip": server["ip"],

                "status": "ONLINE",

                "latency": latency,

                "metrics": metrics
            })

        except Exception as e:

            monitored.append({

                "name": server["name"],

                "ip": server["ip"],

                "status": "OFFLINE",

                "error": str(e),

                "metrics": None
            })

    return render_template(
        "aws_monitor.html",
        servers=monitored
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=9000,
        debug=True
    )