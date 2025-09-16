import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(page_title="Lagos Traffic Congestion", layout="wide")

st.title("🚦 Lagos Traffic Congestion Prediction")
df = pd.read_csv("data/processed/traffic_data.csv")

model = joblib.load("data/models/traffic_model.pkl")

st.subheader("📊 Live Traffic Analytics")
fig = px.histogram(df, x="congestion_level", color="congestion_level")
st.plotly_chart(fig, use_container_width=True)

st.subheader("Make a Prediction")
current_speed = st.number_input("Current Speed (km/h)", 0, 120, 30)
free_flow_speed = st.number_input("Free Flow Speed (km/h)", 0, 120, 60)
confidence = st.slider("Confidence", 0.0, 1.0, 0.8)

if st.button("Predict Congestion"):
    pred = model.predict([[current_speed, free_flow_speed, confidence]])
    st.success(f"Predicted Congestion: {pred}")