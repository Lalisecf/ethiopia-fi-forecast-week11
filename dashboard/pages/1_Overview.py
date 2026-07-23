import streamlit as st
import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Financial Inclusion Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Ethiopia Financial Inclusion Forecast Dashboard")
st.markdown(
    """
    This dashboard summarizes the current state of financial inclusion in Ethiopia
    and presents forecasts for Account Ownership and Digital Financial Usage
    through 2027.
    """
)

# --------------------------------------------------
# Load Forecast Data
# --------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parent.parent

REPORTS_DIR = ROOT_DIR / "reports"

access_forecast = pd.read_csv(REPORTS_DIR / "access_forecast.csv")
usage_forecast = pd.read_csv(REPORTS_DIR / "usage_forecast.csv")

# --------------------------------------------------
# Latest Forecast
# --------------------------------------------------
forecast_2027 = access_forecast.loc[
    access_forecast["year"] == 2027,
    "Base"
].values[0]

# --------------------------------------------------
# Key Metrics
# --------------------------------------------------
st.subheader("Key Financial Inclusion Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Account Ownership",
    value="49%"
)

col2.metric(
    label="Digital Payments",
    value="35%"
)

col3.metric(
    label="Mobile Money",
    value="9.45%"
)

col4.metric(
    label="2027 Forecast",
    value=f"{forecast_2027:.1f}%"
)

st.divider()

# --------------------------------------------------
# Growth Summary
# --------------------------------------------------
st.subheader("Growth Summary")

growth = forecast_2027 - 49

col1, col2 = st.columns(2)

col1.metric(
    "Growth Since 2024",
    f"{growth:.1f} percentage points"
)

col2.metric(
    "Forecast Horizon",
    "2025–2027"
)

# --------------------------------------------------
# P2P / ATM Ratio
# --------------------------------------------------
st.subheader("P2P / ATM Activity")

st.info(
    """
    **P2P/ATM Ratio** measures the transition from traditional ATM usage
    toward digital peer-to-peer payments.

    Higher values indicate increasing adoption of digital financial services
    and stronger financial inclusion.
    """
)

# --------------------------------------------------
# Forecast Preview
# --------------------------------------------------
st.subheader("Forecast Preview")

st.dataframe(
    access_forecast[
        ["year", "Base", "Optimistic", "Pessimistic"]
    ],
    use_container_width=True
)

# --------------------------------------------------
# Dashboard Notes
# --------------------------------------------------
st.markdown("---")

st.markdown(
    """
    ### Dashboard Highlights

    - **Current Account Ownership:** 49%
    - **Digital Payment Adoption:** 35%
    - **Mobile Money Account Ownership:** 9.45%
    - **Forecast Period:** 2025–2027
    - Forecasts combine historical trends with policy and event impacts identified during Task 3.
    """
)