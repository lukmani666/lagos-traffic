import requests
import json
import os
from datetime import datetime
from decouple import config

API_KEY = config("TOMTOM_API_KEY")

def fetch_traffic_flow(lat=6.5244, lon=3.3789, zoom=10):
    """Fetch traffic flow for a given Lagos coordinate"""
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/{zoom}/json"
    params = {"key": API_KEY, "point": f"{lat},{lon}"}
    r = requests.get(url, params=params)
    return r.json()

def save_raw_data():
    data = fetch_traffic_flow()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"data/raw/traffic_{timestamp}.json"
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Saved raw traffic data to {path}")

if __name__ == "__main__":
    save_raw_data()