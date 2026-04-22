import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train():

    data = pd.read_csv("data/system_metrics.csv")

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05
    )

    model.fit(data)

    joblib.dump(model, "ml/model.pkl")

    print("Model trained and saved")

if __name__ == "__main__":
    train()