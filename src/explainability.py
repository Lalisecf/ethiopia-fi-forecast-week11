"""
Model explainability using SHAP.

The core forecasting model (``src/forecast.py``) is a simple linear
trend + rule-based event adjustment, which is already interpretable
(one coefficient). To give a genuinely useful SHAP explanation, this
module instead explains the **event-impact model**: it fits a small
regression of an indicator's period-over-period change on the events
active in that period (one-hot / magnitude-weighted features), and
uses SHAP to answer:

* Which events/features matter most globally for a given indicator?
* Why did the model attribute a given period's change the way it did?

This mirrors the "association matrix" already built in
``src/event_model.py`` but turns it into a fitted, explainable model
rather than a fixed lookup table.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

try:
    import shap
except ImportError:  # pragma: no cover - shap is an optional/heavy dependency
    shap = None


@dataclass
class ExplainabilityResult:
    """Container for a fitted explainable model and its SHAP values."""

    model: RandomForestRegressor
    feature_names: list[str]
    shap_values: "np.ndarray | None"
    explainer: "object | None"


def build_event_feature_matrix(
    association_matrix: pd.DataFrame, indicator_code: str
) -> pd.DataFrame:
    """Turn the event x indicator association matrix into a feature
    matrix (one row per event, one column per indicator) suitable for
    a supervised model that predicts a single indicator's impact
    magnitude from all events' characteristics.

    This is intentionally a thin wrapper so it can be swapped for a
    richer feature set (event category, lag, confidence) later
    without changing the explainability pipeline below.
    """
    features = association_matrix.fillna(0).copy()
    if indicator_code not in features.columns:
        raise KeyError(f"Indicator '{indicator_code}' not found in association matrix.")
    return features


def fit_explainable_model(
    features: pd.DataFrame, target_col: str, random_state: int = 42
) -> RandomForestRegressor:
    """Fit a small RandomForestRegressor predicting ``target_col``
    from the remaining columns. Tree ensembles work well with SHAP's
    fast ``TreeExplainer`` and tolerate the small-N setting typical of
    this dataset.
    """
    x = features.drop(columns=[target_col])
    y = features[target_col]
    model = RandomForestRegressor(
        n_estimators=200, max_depth=4, random_state=random_state
    )
    model.fit(x, y)
    return model


def explain_model(
    model: RandomForestRegressor, x: pd.DataFrame
) -> ExplainabilityResult:
    """Compute SHAP values for a fitted tree model.

    Returns an ``ExplainabilityResult`` with ``shap_values=None`` if
    the optional ``shap`` package is not installed, so callers can
    degrade gracefully (e.g. show feature_importances_ instead).
    """
    if shap is None:
        return ExplainabilityResult(
            model=model,
            feature_names=list(x.columns),
            shap_values=None,
            explainer=None,
        )

    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(x)
    return ExplainabilityResult(
        model=model,
        feature_names=list(x.columns),
        shap_values=shap_values,
        explainer=explainer,
    )


def global_feature_importance(result: ExplainabilityResult) -> pd.Series:
    """Mean absolute SHAP value per feature = global importance ranking.

    Falls back to the model's built-in ``feature_importances_`` if
    SHAP values aren't available.
    """
    if result.shap_values is not None:
        importance = np.abs(result.shap_values).mean(axis=0)
    else:
        importance = result.model.feature_importances_
    return pd.Series(importance, index=result.feature_names).sort_values(
        ascending=False
    )
