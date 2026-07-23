import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="Forecasts",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Financial Inclusion Forecasts")

st.markdown("""
Explore historical trends, baseline forecasts, event-augmented forecasts,
and projected financial inclusion milestones.
""")

# -----------------------------------------------------
# Load Data
# -----------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent

REPORTS_DIR = ROOT_DIR / "reports"
DATA_DIR = ROOT_DIR / "data" / "processed"

forecast = pd.read_csv(REPORTS_DIR / "access_forecast.csv")

df = pd.read_csv(DATA_DIR / "ethiopia_fi_unified_data.csv")

# Historical observations
access = df[
    (df["record_type"] == "observation") &
    (df["indicator_code"] == "ACC_OWNERSHIP")
].copy()

access["observation_date"] = pd.to_datetime(access["observation_date"])
access["year"] = access["observation_date"].dt.year

# -----------------------------------------------------
# Step 11 - Model Selector
# -----------------------------------------------------
model = st.selectbox(
    "Forecast Model",
    [
        "Baseline",
        "Event-Augmented"
    ]
)

forecast_column = "Base"

if model == "Event-Augmented":
    forecast_column = "Event"

# -----------------------------------------------------
# Step 10 - Forecast Visualization
# -----------------------------------------------------
st.subheader("Historical vs Forecast")

fig = go.Figure()

# Historical
fig.add_trace(
    go.Scatter(
        x=access["year"],
        y=access["value_numeric"],
        mode="lines+markers",
        name="Historical"
    )
)

# Forecast
fig.add_trace(
    go.Scatter(
        x=forecast["year"],
        y=forecast[forecast_column],
        mode="lines+markers",
        name=model
    )
)

# Confidence Interval
fig.add_trace(
    go.Scatter(
        x=list(forecast["year"]) + list(forecast["year"][::-1]),
        y=list(forecast["upper"]) + list(forecast["lower"][::-1]),
        fill="toself",
        fillcolor="rgba(0,100,255,0.20)",
        line=dict(color="rgba(255,255,255,0)"),
        hoverinfo="skip",
        showlegend=True,
        name="95% Confidence Interval"
    )
)

fig.update_layout(
    title="Account Ownership Forecast",
    xaxis_title="Year",
    yaxis_title="Account Ownership (%)",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------------------------------
# Step 12 - Projected Milestones
# -----------------------------------------------------
st.subheader("Projected Milestones")

milestones = pd.DataFrame({
    "Year": [2025, 2026, 2027],
    "Target": [50, 54, 58]
})

timeline = go.Figure()

timeline.add_trace(
    go.Scatter(
        x=milestones["Year"],
        y=milestones["Target"],
        mode="lines+markers+text",
        text=[f"{v}%" for v in milestones["Target"]],
        textposition="top center",
        name="Milestone"
    )
)

timeline.update_layout(
    title="Projected Financial Inclusion Milestones",
    xaxis_title="Year",
    yaxis_title="Account Ownership (%)"
)

st.plotly_chart(
    timeline,
    use_container_width=True
)

# -----------------------------------------------------
# Forecast Table
# -----------------------------------------------------
st.subheader("Forecast Table")

st.dataframe(
    forecast,
    use_container_width=True
)