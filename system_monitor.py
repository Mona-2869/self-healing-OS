import psutil
import pandas as pd
import time

def get_system_metrics():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())

    return [cpu, memory, disk, processes]


def collect_data():

    data = []

    while True:

        metrics = get_system_metrics()
        data.append(metrics)

        df = pd.DataFrame(
            data,
            columns=["cpu","memory","disk","processes"]
        )

        df.to_csv("data/system_metrics.csv", index=False)

        print("Metrics:", metrics)

        time.sleep(5)


if __name__ == "__main__":
    collect_data()