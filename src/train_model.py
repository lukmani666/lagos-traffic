import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    df = pd.read_csv("data/processed/traffic_data.csv")
    X = df[["current_speed", "free_flow_speed", "confidence"]]
    y = df["congestion_level"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    acc = model.score(X_test, y_test)
    print(f"Model Accuracy: {acc:.2f}")

    joblib.dump(model, "data/models/traffic_model.pkl")

if __name__ == "__main__":
    train_model()