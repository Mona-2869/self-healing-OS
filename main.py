import time
import psutil
from ml.detect_anomaly import model, pd
from healing.self_heal import heal_cpu, heal_memory

def get_system_data():
    return {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "processes": len(psutil.pids())
    }

def run_system():
    print("🚀 AI Self-Healing OS Running...\n")

    while True:
        data = get_system_data()
        df = pd.DataFrame([data])

        prediction = model.predict(df)

        print(f"System Data: {data}")

        if prediction[0] == -1:
            print("⚠ Anomaly Detected!")
            
            if data["cpu"] > 80:
                heal_cpu()
            if data["memory"] > 80:
                heal_memory()
        else:
            print("✅ System Normal")

        print("----------------------")
        time.sleep(5)

if __name__ == "__main__":
    run_system()