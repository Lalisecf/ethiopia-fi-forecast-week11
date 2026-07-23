import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from sidebar import render_sidebar

render_sidebar()

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="Financial Inclusion Trends",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Financial Inclusion Trends")

st.markdown("""
Explore historical trends and compare key financial inclusion indicators
across Ethiopia's financial ecosystem.
""")

# -----------------------------------------------------
# Load Dataset
# -----------------------------------------------------
ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = ROOT_DIR / "data" / "processed" / "ethiopia_fi_enriched.csv"

df = pd.read_csv(DATA_PATH)

# -----------------------------------------------------
# Prepare Observation Data
# -----------------------------------------------------
obs = df[df["record_type"] == "observation"].copy()

obs["observation_date"] = pd.to_datetime(
    obs["observation_date"],
    format="mixed",
    errors="coerce"
)

obs["year"] = obs["observation_date"].dt.year

# =====================================================
# Step 8 - Date Range Selector
# =====================================================

st.sidebar.header("Filters")

years = st.sidebar.slider(
    "Select Year Range",
    min_value=2011,
    max_value=2027,
    value=(2011, 2027)
)

filtered = obs[
    (obs["year"] >= years[0]) &
    (obs["year"] <= years[1])
]

# =====================================================
# Step 7 - Account Ownership Trend
# =====================================================

st.subheader("Account Ownership Trend")

access = filtered[
    filtered["indicator_code"] == "ACC_OWNERSHIP"
]

fig = px.line(
    access,
    x="year",
    y="value_numeric",
    markers=True,
    title="Account Ownership Rate (2011–2027)"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Account Ownership (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =====================================================
# Digital Payment Trend
# =====================================================

digital = filtered[
    filtered["indicator_code"] == "USG_ACTIVE_RATE"
]

if not digital.empty:

    fig = px.line(
        digital,
        x="year",
        y="value_numeric",
        markers=True,
        title="Digital Payment Usage"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================================
# Step 9 - Financial Channel Comparison
# =====================================================

st.subheader("Financial Channel Comparison")

comparison = filtered[
    filtered["indicator_code"].isin([
        "ACC_BRANCH",
        "ACC_MM_ACCOUNT",
        "USG_ACTIVE_RATE"
    ])
].copy()

comparison["Channel"] = comparison["indicator_code"].map({
    "ACC_BRANCH": "Banks",
    "ACC_MM_ACCOUNT": "Mobile Money",
    "USG_ACTIVE_RATE": "Digital Payments"
})

if not comparison.empty:

    fig = px.bar(
        comparison,
        x="Channel",
        y="value_numeric",
        color="Channel",
        text="value_numeric",
        title="Comparison of Financial Channels"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        showlegend=False,
        yaxis_title="Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

else:
    st.warning("No comparison data available.")

# =====================================================
# Raw Data
# =====================================================

with st.expander("View Filtered Data"):

    st.dataframe(
        filtered,
        use_container_width=True
    )