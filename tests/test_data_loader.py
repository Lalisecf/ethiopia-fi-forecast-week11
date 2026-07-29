from __future__ import annotations

import pandas as pd
import pytest

from src.data_loader import (
    assess_data_quality,
    filter_by_record_type,
    get_events,
    get_indicator_series,
    get_observations,
)


def test_filter_by_record_type_returns_only_matching_rows(sample_unified_data):
    observations = filter_by_record_type(sample_unified_data, "observation")
    assert (observations["record_type"] == "observation").all()
    assert len(observations) == 3


def test_filter_by_record_type_missing_column_raises():
    bad_df = pd.DataFrame({"foo": [1, 2, 3]})
    with pytest.raises(KeyError):
        filter_by_record_type(bad_df, "observation")


def test_get_observations_parses_dates(sample_unified_data):
    observations = get_observations(sample_unified_data)
    assert pd.api.types.is_datetime64_any_dtype(observations["observation_date"])
    assert len(observations) == 3


def test_get_events_sorted_by_date(sample_unified_data):
    events = get_events(sample_unified_data)
    dates = events["observation_date"].tolist()
    assert dates == sorted(dates)
    assert len(events) == 2


def test_get_indicator_series_extracts_correct_indicator(sample_unified_data):
    series = get_indicator_series(sample_unified_data, "ACC_OWNERSHIP")
    assert list(series["year"]) == [2017, 2021, 2024]
    assert list(series["value_numeric"]) == [35.0, 46.0, 49.0]


def test_get_indicator_series_unknown_indicator_returns_empty(sample_unified_data):
    series = get_indicator_series(sample_unified_data, "NOT_A_REAL_CODE")
    assert series.empty


def test_assess_data_quality_reports_expected_keys(sample_unified_data):
    quality = assess_data_quality(sample_unified_data)
    assert quality["n_rows"] == 5
    assert quality["n_duplicates"] == 0
    assert "observation" in quality["record_type_counts"]
    assert quality["record_type_counts"]["observation"] == 3
