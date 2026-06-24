from flask import Flask, jsonify
from collections import deque
import psutil
import socket
import platform
import datetime
import threading
import time

app = Flask(__name__)

cpu_history = deque(maxlen=20)
memory_history = deque(maxlen=20)
disk_history = deque(maxlen=20)


def collect_metrics():

    while True:

        cpu_history.append(
            psutil.cpu_percent()
        )

        memory_history.append(
            psutil.virtual_memory().percent
        )

        disk_history.append(
            psutil.disk_usage("/").percent
        )

        time.sleep(5)


@app.route("/")
def home():

    return {
        "project": "CloudOps Monitor",
        "status": "running"
    }


@app.route("/metrics")
def metrics():

    cpu = psutil.cpu_percent()

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    boot_time = datetime.datetime.fromtimestamp(
        psutil.boot_time()
    )

    uptime_hours = round(
        (
            datetime.datetime.now()
            - boot_time
        ).total_seconds() / 3600,
        2
    )

    try:

        load = psutil.getloadavg()

        load_average = {
            "1min": round(load[0],2),
            "5min": round(load[1],2),
            "15min": round(load[2],2)
        }

    except:

        load_average = {
            "1min":0,
            "5min":0,
            "15min":0
        }

    return jsonify({

        "hostname": socket.gethostname(),

        "os": platform.system(),

        "os_version": platform.version(),

        "cpu_percent": cpu,

        "memory": {
            "total_gb": round(memory.total/(1024**3),2),
            "used_percent": memory.percent
        },

        "disk": {
            "total_gb": round(disk.total/(1024**3),2),
            "used_percent": disk.percent
        },

        "boot_time": str(boot_time),

        "uptime_hours": uptime_hours,

        "load_average": load_average,

        "timestamp": str(datetime.datetime.now()),

        "history": {

            "cpu": list(cpu_history),

            "memory": list(memory_history),

            "disk": list(disk_history)

        }

    })


if __name__ == "__main__":

    threading.Thread(
        target=collect_metrics,
        daemon=True
    ).start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )