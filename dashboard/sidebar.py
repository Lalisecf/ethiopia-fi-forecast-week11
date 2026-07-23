import streamlit as st

def render_sidebar():
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
        - Ethiopia Financial Inclusion Dataset
        - Global Findex
        - National Bank of Ethiopia
        - Telebirr and M-Pesa indicators

        **Methodology**
        - Exploratory Data Analysis
        - Linear Regression
        - Event-Augmented Forecasting
        - Scenario Analysis
        - Confidence Intervals
        """
    )