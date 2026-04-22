import psutil
import os
import time

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80


def heal_cpu():
    print("⚠ High CPU usage detected!")
    print("🛠 Attempting CPU self-healing...")

    # Kill high CPU consuming processes
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['cpu_percent'] > 50:
                print(f"Stopping process: {proc.info['name']} (PID {proc.info['pid']})")
                os.kill(proc.info['pid'], 9)
        except:
            pass

    print("✅ CPU healing completed\n")


def heal_memory():
    print("⚠ High memory usage detected!")
    print("🛠 Clearing system cache...")

    os.system("sync; echo 3 | sudo tee /proc/sys/vm/drop_caches")

    print("✅ Memory cache cleared\n")


def monitor_system():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent

        print(f"CPU Usage: {cpu}%")
        print(f"Memory Usage: {memory}%")

        if cpu > CPU_THRESHOLD:
            heal_cpu()

        if memory > MEMORY_THRESHOLD:
            heal_memory()

        print("✅ System running...\n")
        time.sleep(5)


if __name__ == "__main__":
    print("🚀 AI Self-Healing System Started...\n")
    monitor_system()