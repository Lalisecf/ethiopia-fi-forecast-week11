import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path
from sidebar import render_sidebar

render_sidebar()

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="Future Projections",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 Future Financial Inclusion Projections")

st.markdown("""
Explore Ethiopia's projected progress toward national financial inclusion
targets under different forecasting scenarios.
""")

# -----------------------------------------------------
# Load Forecast Data
# -----------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[2]

REPORTS_DIR = ROOT_DIR / "reports"

forecast = pd.read_csv(REPORTS_DIR / "access_forecast.csv")

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------
st.sidebar.title("Navigation")

st.sidebar.page_link("app.py", label="🏠 Home")
st.sidebar.page_link("pages/1_Overview.py", label="Overview")
st.sidebar.page_link("pages/2_Trends.py", label="Trends")
st.sidebar.page_link("pages/3_Forecasts.py", label="Forecasts")
st.sidebar.page_link("pages/4_Projections.py", label="Projections")

st.sidebar.markdown("---")

st.sidebar.header("About")

st.sidebar.info(
"""
**Dataset**

Global Findex indicators, National Bank of Ethiopia,
Telebirr, M-Pesa, GSMA and other public financial
inclusion datasets.

---

**Methodology**

• Historical trend analysis

• Linear Regression Forecasting

• Event-Augmented Forecasting

• Scenario Analysis

• Confidence Intervals
"""
)

# =====================================================
# Step 14
# Scenario Selector
# =====================================================

st.subheader("Forecast Scenario")

scenario = st.radio(
    "Scenario",
    [
        "Optimistic",
        "Base",
        "Pessimistic"
    ],
    horizontal=True
)

column = scenario

# =====================================================
# Step 13
# Gauge
# =====================================================

forecast_2027 = forecast.loc[
    forecast["Year"] == 2027,
    column
].values[0]

fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=forecast_2027,
        title={
            "text": "Progress Toward 60% Financial Inclusion"
        },
        gauge={
            "axis": {
                "range": [0, 60]
            },
            "bar": {
                "color": "green"
            },
            "steps": [
                {
                    "range": [0, 60],
                    "color": "#E8F5E9"
                }
            ],
            "threshold": {
                "line": {
                    "color": "red",
                    "width": 4
                },
                "value": 60
            }
        }
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.metric(
    "2027 Forecast",
    f"{forecast_2027:.1f}%"
)

st.metric(
    "National Target",
    "60%"
)

# =====================================================
# Scenario Plot
# =====================================================

st.subheader("Scenario Projection")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=forecast["Year"],
        y=forecast[column],
        mode="lines+markers",
        name=scenario
    )
)

fig.update_layout(
    title=f"{scenario} Forecast",
    xaxis_title="Year",
    yaxis_title="Account Ownership (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# Step 15
# Consortium Questions
# =====================================================

st.subheader("Policy Insights")

with st.expander("What drives financial inclusion?"):

    st.markdown("""
- Expansion of Telebirr
- M-Pesa market entry
- Mobile internet penetration
- Digital ID (Fayda)
- National Financial Inclusion Strategy II
- Financial infrastructure improvements
""")

with st.expander("Largest Events Affecting Growth"):

    st.markdown("""
- Telebirr Launch
- M-Pesa Launch
- Fayda Digital ID rollout
- Interoperability initiatives
- Payment infrastructure expansion
""")

with st.expander("Future Outlook"):

    st.markdown("""
The forecasts indicate continued growth in financial inclusion
between 2025 and 2027. Event-augmented projections suggest
stronger growth where digital financial services continue
expanding and supporting infrastructure improves.
""")

with st.expander("Policy Impact"):

    st.markdown("""
Government policy plays a critical role through:

- Digital financial inclusion initiatives
- Mobile money regulation
- Digital identity expansion
- National payment infrastructure
- Financial sector modernization
""")

# =====================================================
# Step 16
# Download Buttons
# =====================================================

st.subheader("Download Forecast Results")

col1, col2 = st.columns(2)

with col1:

    st.download_button(
        "📥 Download Access Forecast",
        forecast.to_csv(index=False),
        file_name="access_forecast.csv",
        mime="text/csv"
    )

with col2:

    usage = pd.read_csv(REPORTS_DIR / "usage_forecast.csv")

    st.download_button(
        "📥 Download Usage Forecast",
        usage.to_csv(index=False),
        file_name="usage_forecast.csv",
        mime="text/csv"
    )