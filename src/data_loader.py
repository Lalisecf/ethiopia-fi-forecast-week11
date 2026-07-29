"""
Data loading and cleaning utilities for the unified financial inclusion
dataset.

Refactored out of ``notebooks/task1_data_exploration.ipynb`` into
reusable, type-hinted, independently-testable functions.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from .config import (
    ENRICHED_DATA_FILE,
    ENRICHED_IMPACT_LINKS_FILE,
    IMPACT_SHEET_NAME,
    MAIN_SHEET_NAME,
    RAW_EXCEL_FILE,
    RECORD_TYPE_EVENT,
    RECORD_TYPE_OBSERVATION,
    REFERENCE_CODES_FILE,
)


def load_raw_dataset(
    excel_file: Path = RAW_EXCEL_FILE,
    reference_codes_file: Path = REFERENCE_CODES_FILE,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load the three raw source files.

    Parameters
    ----------
    excel_file:
        Path to ``ethiopia_fi_unified_data.xlsx``.
    reference_codes_file:
        Path to ``reference_codes.csv``.

    Returns
    -------
    (data, impact_links, reference_codes)
        Three dataframes: the main unified-schema sheet, the impact
        links sheet, and the reference codes lookup table.
    """
    data = pd.read_excel(excel_file, sheet_name=MAIN_SHEET_NAME)
    impact_links = pd.read_excel(excel_file, sheet_name=IMPACT_SHEET_NAME)
    reference_codes = pd.read_csv(reference_codes_file)
    return data, impact_links, reference_codes


def load_enriched_dataset(
    enriched_data_file: Path = ENRICHED_DATA_FILE,
    enriched_impact_links_file: Path = ENRICHED_IMPACT_LINKS_FILE,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Load the processed/enriched CSVs produced by Task 1.

    Returns
    -------
    (data, impact_links)
    """
    data = pd.read_csv(enriched_data_file)
    impact_links = pd.read_csv(enriched_impact_links_file)
    return data, impact_links


def filter_by_record_type(data: pd.DataFrame, record_type: str) -> pd.DataFrame:
    """Return only the rows of ``data`` matching ``record_type``.

    Parameters
    ----------
    data:
        The unified-schema dataframe.
    record_type:
        One of ``observation``, ``event``, ``impact_link``, ``target``.
    """
    if "record_type" not in data.columns:
        raise KeyError("Expected a 'record_type' column in the dataframe.")
    return data[data["record_type"] == record_type].copy()


def get_observations(data: pd.DataFrame) -> pd.DataFrame:
    """Convenience wrapper: return only ``observation`` records with a
    parsed ``observation_date`` column."""
    observations = filter_by_record_type(data, RECORD_TYPE_OBSERVATION)
    observations["observation_date"] = pd.to_datetime(
    observations["observation_date"],
    format="mixed",
    errors="coerce"
    )
    return observations


def get_events(data: pd.DataFrame) -> pd.DataFrame:
    """Convenience wrapper: return only ``event`` records sorted by date."""
    events = filter_by_record_type(data, RECORD_TYPE_EVENT)
    events["observation_date"] = pd.to_datetime(events["observation_date"])
    return events.sort_values("observation_date")


def get_indicator_series(
    data: pd.DataFrame, indicator_code: str
) -> pd.DataFrame:
    """Return the historical time series (year, value_numeric) for a
    single indicator code, extracted from the observation records.

    Parameters
    ----------
    data:
        The unified-schema dataframe (raw or enriched).
    indicator_code:
        e.g. ``"ACC_OWNERSHIP"``.
    """
    observations = get_observations(data)
    series = observations[observations["indicator_code"] == indicator_code].copy()
    series["year"] = series["observation_date"].dt.year
    return series.sort_values("year").reset_index(drop=True)


def assess_data_quality(data: pd.DataFrame) -> dict[str, object]:
    """Compute basic data-quality diagnostics used in Task 1/2.

    Returns a dictionary with missing-value percentages, duplicate row
    count, and per-``record_type`` counts, so it can be asserted on in
    tests or rendered in the dashboard.
    """
    return {
        "n_rows": len(data),
        "n_duplicates": int(data.duplicated().sum()),
        "missing_pct_by_column": (data.isnull().mean() * 100).round(2).to_dict(),
        "record_type_counts": data["record_type"].value_counts().to_dict(),
    }


def save_processed_dataset(
    data: pd.DataFrame,
    impact_links: pd.DataFrame,
    enriched_data_file: Path = ENRICHED_DATA_FILE,
    enriched_impact_links_file: Path = ENRICHED_IMPACT_LINKS_FILE,
) -> None:
    """Persist the enriched dataset + impact links to ``data/processed``."""
    enriched_data_file.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(enriched_data_file, index=False)
    impact_links.to_csv(enriched_impact_links_file, index=False)
