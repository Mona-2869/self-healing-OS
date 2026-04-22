import psutil
import time
import os
from root_cause import find_root_cause

while True:

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    print("CPU:", cpu, "Memory:", memory)

    # anomaly condition
    if cpu > 80 or memory > 85:

        print("⚠️ Anomaly Detected")

        cause = find_root_cause()

        if cause:

            print("Root Cause Found")
            print("Process:", cause['process'])
            print("PID:", cause['pid'])
            print("CPU Usage:", cause['cpu'])
            print("Memory Usage:", cause['memory'])

            # 🔴 OPTIONAL STEP (AUTO HEALING)
            os.kill(cause['pid'], 9)

            print("Self-Healing Action: Process terminated")

    time.sleep(5)