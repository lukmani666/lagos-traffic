import pandas as pd
import glob
import json

def process_raw_data():
    files = glob.glob("data/raw/*.json")
    records = []

    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
            seg = data.get("flowSegmentData", {})
            records.append({
                "timestamp": file.split("_")[-1].replace(".json", ""),
                "current_speed": seg.get("currentSpeed"),
                "free_flow_speed": seg.get("freeFlowSpeed"),
                "confidence": seg.get("confidence"),
                "road_closure": seg.get("roadClosure"),
            })
    
    df = pd.DataFrame(records)
    df["congestion_ratio"] = df["current_speed"] / df["free_flow_speed"]
    df["congestion_level"] = pd.cut(df["congestion_ratio"],
                                    bins=[0,0.25,0.5,0.75,1],
                                    labels=["Severe", "Heavy", "Moderate", "Free flow"])
    df.to_csv("data/processed/traffic_data.csv", index=False)
    print("Processed data saved to data/processed/trafic_data.csv")

    return df

if __name__ == "__main__":
    process_raw_data()