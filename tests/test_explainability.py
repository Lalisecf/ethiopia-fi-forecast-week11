from __future__ import annotations

import pandas as pd
import pytest

from src.explainability import (
    build_event_feature_matrix,
    explain_model,
    fit_explainable_model,
    global_feature_importance,
)


@pytest.fixture
def sample_association_matrix() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "ACC_OWNERSHIP": [3.0, 1.5, 0.0, 2.0],
            "USG_P2P_COUNT": [5.0, 0.0, 4.0, 1.0],
            "ACC_MM_ACCOUNT": [2.0, 3.0, 1.0, 0.5],
        },
        index=["EVT_0001", "EVT_0002", "EVT_0003", "EVT_0004"],
    )


def test_build_event_feature_matrix_raises_for_unknown_indicator(
    sample_association_matrix,
):
    with pytest.raises(KeyError):
        build_event_feature_matrix(sample_association_matrix, "NOT_REAL")


def test_fit_explainable_model_predicts_reasonable_values(
    sample_association_matrix,
):
    features = build_event_feature_matrix(sample_association_matrix, "ACC_OWNERSHIP")
    model = fit_explainable_model(features, target_col="ACC_OWNERSHIP")
    x = features.drop(columns=["ACC_OWNERSHIP"])
    preds = model.predict(x)
    assert len(preds) == len(features)
    assert (preds >= 0).all()


def test_global_feature_importance_sums_are_nonnegative(sample_association_matrix):
    features = build_event_feature_matrix(sample_association_matrix, "ACC_OWNERSHIP")
    model = fit_explainable_model(features, target_col="ACC_OWNERSHIP")
    x = features.drop(columns=["ACC_OWNERSHIP"])
    result = explain_model(model, x)
    importance = global_feature_importance(result)
    assert (importance >= 0).all()
    assert set(importance.index) == set(x.columns)
