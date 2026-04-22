from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Self-Healing OS Dashboard Running"

@app.route("/metrics")
def metrics():
    data = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)