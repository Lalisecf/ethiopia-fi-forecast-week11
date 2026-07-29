from __future__ import annotations

import pandas as pd

from src.data_loader import get_events
from src.event_model import (
    build_association_matrix,
    compute_impact_score,
    compute_indicator_impact_scores,
    get_event_bonus,
    merge_events_with_impacts,
    normalize_association_matrix,
    validate_against_history,
)


def test_compute_impact_score_maps_categorical_labels_to_signed_numeric():
    links = pd.DataFrame(
        {
            "impact_magnitude": ["high", "medium", "low"],
            "impact_direction": ["increase", "decrease", "neutral"],
        }
    )
    scores = compute_impact_score(links)
    assert list(scores) == [3 * 1, 2 * -1, 1 * 0]


def test_compute_impact_score_unknown_label_is_nan():
    links = pd.DataFrame(
        {"impact_magnitude": ["extreme"], "impact_direction": ["increase"]}
    )
    scores = compute_impact_score(links)
    assert scores.isna().all()


def test_merge_events_with_impacts_joins_on_parent_id(
    sample_unified_data, sample_impact_links
):
    events = get_events(sample_unified_data)
    merged = merge_events_with_impacts(events, sample_impact_links)
    assert len(merged) == len(sample_impact_links)
    assert "notes" in merged.columns
    assert merged.loc[merged["parent_id"] == "EVT_0001", "notes"].iloc[0] == (
        "Telebirr launch"
    )


def test_build_association_matrix_shape(sample_impact_links):
    matrix = build_association_matrix(sample_impact_links)
    # 2 unique events (rows) x 2 unique indicators (columns)
    assert matrix.shape == (2, 2)
    assert "ACC_OWNERSHIP" in matrix.columns
    assert "USG_P2P_COUNT" in matrix.columns


def test_normalize_association_matrix_columns_sum_to_one(sample_impact_links):
    matrix = build_association_matrix(sample_impact_links)
    normalized = normalize_association_matrix(matrix)
    col_sums = normalized.abs().sum(axis=0)
    for total in col_sums:
        assert abs(total - 1.0) < 1e-9 or total == 0


def test_compute_indicator_impact_scores_returns_positive_scores(
    sample_impact_links,
):
    matrix = build_association_matrix(sample_impact_links)
    normalized = normalize_association_matrix(matrix)
    scores = compute_indicator_impact_scores(normalized)
    assert scores["ACC_OWNERSHIP"] > 0
    assert scores["USG_P2P_COUNT"] > 0


def test_get_event_bonus_falls_back_to_default():
    scores = {"ACC_OWNERSHIP": 0.8}
    assert get_event_bonus(scores, "ACC_OWNERSHIP") == 0.8
    assert get_event_bonus(scores, "UNKNOWN_CODE") == 0.0
    assert get_event_bonus(scores, "UNKNOWN_CODE", default=1.5) == 1.5


def test_validate_against_history_within_tolerance():
    assert validate_against_history(predicted_change=4.5, observed_change=4.75)
    assert not validate_against_history(
        predicted_change=4.5, observed_change=20.0, tolerance_pp=5.0
    )
