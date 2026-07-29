"""
Project-wide configuration objects and named constants.

Centralizing these values here removes the "magic numbers" that were
scattered across the Week 11 notebooks (e.g. hard-coded confidence
z-scores, scenario bump percentages, file paths) and gives every
module a single, typed source of truth.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


# --------------------------------------------------------------------------
# Filesystem layout
# --------------------------------------------------------------------------

PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
RAW_DATA_DIR: Path = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR: Path = PROJECT_ROOT / "data" / "processed"
REPORTS_DIR: Path = PROJECT_ROOT / "reports"
FIGURES_DIR: Path = REPORTS_DIR / "figures"

RAW_EXCEL_FILE: Path = RAW_DATA_DIR / "ethiopia_fi_unified_data.xlsx"
REFERENCE_CODES_FILE: Path = RAW_DATA_DIR / "reference_codes.csv"
ENRICHED_DATA_FILE: Path = PROCESSED_DATA_DIR / "ethiopia_fi_enriched.csv"
ENRICHED_IMPACT_LINKS_FILE: Path = PROCESSED_DATA_DIR / "impact_links_enriched.csv"

MAIN_SHEET_NAME: str = "ethiopia_fi_unified_data"
IMPACT_SHEET_NAME: str = "Impact_sheet"


# --------------------------------------------------------------------------
# Schema / domain constants (replace "magic strings" from the notebooks)
# --------------------------------------------------------------------------

RECORD_TYPE_OBSERVATION: str = "observation"
RECORD_TYPE_EVENT: str = "event"
RECORD_TYPE_IMPACT_LINK: str = "impact_link"
RECORD_TYPE_TARGET: str = "target"

INDICATOR_ACCESS: str = "ACC_OWNERSHIP"
INDICATOR_MOBILE_MONEY: str = "ACC_MM_ACCOUNT"
INDICATOR_USAGE_DIGITAL_PAYMENT: str = "USG_DIGITAL_PAYMENT"
INDICATOR_USAGE_P2P: str = "USG_P2P_COUNT"

FORECAST_YEARS: tuple[int, ...] = (2025, 2026, 2027)


# --------------------------------------------------------------------------
# Forecasting configuration
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class ForecastConfig:
    """Configuration for the trend + event-augmented forecasting model.

    Replaces the magic numbers that were hard-coded inline in the Week 11
    notebook (e.g. ``1.96``, ``1.10``, ``0.90``, ``+3``, ``-3``).
    """

    forecast_years: tuple[int, ...] = FORECAST_YEARS
    confidence_z_score: float = 1.96          # 95% CI multiplier
    optimistic_multiplier: float = 1.10        # +10% vs. base scenario
    pessimistic_multiplier: float = 0.90       # -10% vs. base scenario
    access_scenario_band_pp: float = 3.0       # +/- pp for Access scenarios
    usage_scenario_band_pp: float = 4.0        # +/- pp for Usage scenarios


@dataclass(frozen=True)
class IndicatorSpec:
    """Describes a single indicator to be modeled/forecast."""

    indicator_code: str
    display_name: str
    pillar: str


ACCESS_INDICATOR = IndicatorSpec(
    indicator_code=INDICATOR_ACCESS,
    display_name="Account Ownership Rate",
    pillar="ACCESS",
)

USAGE_INDICATOR = IndicatorSpec(
    indicator_code=INDICATOR_USAGE_P2P,
    display_name="Digital Payment / P2P Usage",
    pillar="USAGE",
)


@dataclass
class AppConfig:
    """Top-level configuration object combining all sub-configs.

    A single instance of this can be constructed once (e.g. in the
    dashboard or a notebook) and passed into every function instead of
    each function re-deriving paths and constants independently.
    """

    forecast: ForecastConfig = field(default_factory=ForecastConfig)
    raw_excel_file: Path = RAW_EXCEL_FILE
    reference_codes_file: Path = REFERENCE_CODES_FILE
    enriched_data_file: Path = ENRICHED_DATA_FILE
    enriched_impact_links_file: Path = ENRICHED_IMPACT_LINKS_FILE
    figures_dir: Path = FIGURES_DIR
    reports_dir: Path = REPORTS_DIR
