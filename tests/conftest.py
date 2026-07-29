"""Shared pytest fixtures: small synthetic datasets that mirror the
unified schema, so tests run fast and don't depend on the real
(large) Excel source file."""

from __future__ import annotations

import pandas as pd
import pytest


@pytest.fixture
def sample_unified_data() -> pd.DataFrame:
    """A tiny unified-schema dataframe with observation + event rows."""
    return pd.DataFrame(
        [
            {
                "record_id": "OBS_0001",
                "record_type": "observation",
                "indicator_code": "ACC_OWNERSHIP",
                "value_numeric": 35.0,
                "observation_date": "2017-12-31",
            },
            {
                "record_id": "OBS_0002",
                "record_type": "observation",
                "indicator_code": "ACC_OWNERSHIP",
                "value_numeric": 46.0,
                "observation_date": "2021-12-31",
            },
            {
                "record_id": "OBS_0003",
                "record_type": "observation",
                "indicator_code": "ACC_OWNERSHIP",
                "value_numeric": 49.0,
                "observation_date": "2024-12-31",
            },
            {
                "record_id": "EVT_0001",
                "record_type": "event",
                "category": "product_launch",
                "indicator_code": None,
                "value_numeric": None,
                "observation_date": "2021-05-11",
                "notes": "Telebirr launch",
            },
            {
                "record_id": "EVT_0002",
                "record_type": "event",
                "category": "market_entry",
                "indicator_code": None,
                "value_numeric": None,
                "observation_date": "2023-08-01",
                "notes": "M-Pesa entry",
            },
        ]
    )


@pytest.fixture
def sample_impact_links() -> pd.DataFrame:
    """A tiny impact_link dataframe referencing the sample events above."""
    return pd.DataFrame(
        [
            {
                "record_id": "IMP_0001",
                "parent_id": "EVT_0001",
                "related_indicator": "ACC_OWNERSHIP",
                "impact_direction": "positive",
                "impact_magnitude": 3.0,
                "lag_months": 6,
            },
            {
                "record_id": "IMP_0002",
                "parent_id": "EVT_0002",
                "related_indicator": "ACC_OWNERSHIP",
                "impact_direction": "positive",
                "impact_magnitude": 1.5,
                "lag_months": 9,
            },
            {
                "record_id": "IMP_0003",
                "parent_id": "EVT_0001",
                "related_indicator": "USG_P2P_COUNT",
                "impact_direction": "positive",
                "impact_magnitude": 5.0,
                "lag_months": 3,
            },
        ]
    )


@pytest.fixture
def sample_indicator_series() -> pd.DataFrame:
    """A tiny (year, value_numeric) time series, as produced by
    ``get_indicator_series``, for forecast-model tests."""
    return pd.DataFrame(
        {
            "year": [2017, 2021, 2024],
            "value_numeric": [35.0, 46.0, 49.0],
        }
    )
