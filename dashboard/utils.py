from pathlib import Path
import pandas as pd

DATA = Path("../data/processed")

REPORTS = Path("../reports")


def load_data():

    df = pd.read_csv(
        DATA/"ethiopia_fi_enriched.csv"
    )

    access = pd.read_csv(
        REPORTS/"access_forecast.csv"
    )

    usage = pd.read_csv(
        REPORTS/"usage_forecast.csv"
    )

    return df,access,usage