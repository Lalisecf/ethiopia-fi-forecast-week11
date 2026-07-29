"""
Application configuration.

This module centralizes project configuration including
data locations, forecast settings, dashboard configuration,
and model parameters.
"""

from dataclasses import dataclass
from pathlib import Path


# -----------------------------------------------------------------------------
# Base Directories
# -----------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = ROOT_DIR / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORTS_DIR = ROOT_DIR / "reports"

FIGURES_DIR = REPORTS_DIR / "figures"

MODELS_DIR = ROOT_DIR / "models"

# -----------------------------------------------------------------------------
# Dataset Configuration
# -----------------------------------------------------------------------------

@dataclass
class DatasetConfig:
    """Dataset file locations."""

    unified_dataset: Path = (
        PROCESSED_DATA_DIR /
        "ethiopia_fi_unified_data.csv"
    )
    unified_excel: Path = RAW_DATA_DIR / "ethiopia_fi_unified_data.xlsx"
    unified_csv: Path = RAW_DATA_DIR / "ethiopia_fi_unified_data.csv"

    reference_codes: Path = (
        RAW_DATA_DIR /
        "reference_codes.csv"
    )

    enriched_dataset: Path = (
        PROCESSED_DATA_DIR /
        "ethiopia_fi_enriched_data.csv"
    )
# -----------------------------------------------------------------------------
# Forecast Configuration
# -----------------------------------------------------------------------------

@dataclass
class ForecastConfig:
    """Forecast parameters."""

    forecast_start_year: int = 2025

    forecast_end_year: int = 2027

    confidence_level: float = 0.95

    random_seed: int = 42


# -----------------------------------------------------------------------------
# Dashboard Configuration
# -----------------------------------------------------------------------------

@dataclass
class DashboardConfig:
    """Dashboard settings."""

    title: str = (
        "Ethiopia Financial Inclusion Dashboard"
    )

    page_icon: str = "📈"

    layout: str = "wide"


# -----------------------------------------------------------------------------
# Global Configuration Object
# -----------------------------------------------------------------------------

dataset_config = DatasetConfig()

forecast_config = ForecastConfig()

dashboard_config = DashboardConfig()