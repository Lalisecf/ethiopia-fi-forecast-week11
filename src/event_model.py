"""
Event-impact modeling utilities.

Refactored out of ``notebooks/task3_event_impact_modeling.ipynb``.
Builds the event <-> indicator association matrix and normalized
impact scores used to augment the trend forecast in
``src/forecast.py``.
"""

from __future__ import annotations

import pandas as pd

from .config import RECORD_TYPE_EVENT

# Default categorical -> numeric mappings used in the Week 11 notebook.
# Centralized here (rather than redefined inline) so both the notebook
# and the dashboard use the same scale.
IMPACT_MAGNITUDE_SCALE: dict[str, int] = {"low": 1, "medium": 2, "high": 3}
IMPACT_DIRECTION_SCALE: dict[str, int] = {"increase": 1, "decrease": -1, "neutral": 0}


def compute_impact_score(
    impact_links: pd.DataFrame,
    magnitude_col: str = "impact_magnitude",
    direction_col: str = "impact_direction",
    magnitude_scale: dict[str, int] = IMPACT_MAGNITUDE_SCALE,
    direction_scale: dict[str, int] = IMPACT_DIRECTION_SCALE,
) -> pd.Series:
    """Convert categorical magnitude/direction labels (e.g. ``"high"``,
    ``"increase"``) into a single signed numeric impact score
    (magnitude x direction), so pivoting/aggregation works as with a
    normal numeric column.

    Rows whose magnitude or direction isn't found in the provided
    scale map to ``NaN`` rather than raising, so unexpected labels
    surface as missing data instead of crashing the pipeline.
    """
    magnitude_numeric = impact_links[magnitude_col].map(magnitude_scale)
    direction_numeric = impact_links[direction_col].map(direction_scale)
    return magnitude_numeric * direction_numeric


def merge_events_with_impacts(
    events: pd.DataFrame, impact_links: pd.DataFrame
) -> pd.DataFrame:
    """Join impact_link records to their parent event via ``parent_id``.

    Parameters
    ----------
    events:
        Dataframe of ``event`` records (see
        :func:`src.data_loader.get_events`).
    impact_links:
        Dataframe of impact_link records (``parent_id`` -> event
        ``record_id``).
    """
    event_columns = ["record_id", "category", "observation_date", "notes"]
    return impact_links.merge(
        events[event_columns],
        left_on="parent_id",
        right_on="record_id",
        how="left",
        suffixes=("_impact", "_event"),
    )


def build_association_matrix(
    impact_links: pd.DataFrame,
    event_col: str = "parent_id",
    indicator_col: str = "related_indicator",
    value_col: str = "impact_magnitude",
) -> pd.DataFrame:
    """Build the Event x Indicator association matrix.

    Rows are events (by ``parent_id``), columns are indicator codes,
    and cell values are the estimated impact magnitude of that event
    on that indicator.
    """
    matrix = impact_links.pivot_table(
        index=event_col,
        columns=indicator_col,
        values=value_col,
        aggfunc="mean",
    )
    return matrix


def normalize_association_matrix(matrix: pd.DataFrame) -> pd.DataFrame:
    """Normalize each indicator column so magnitudes are comparable
    across indicators measured on different scales.

    Missing values are treated as "no effect" (0).
    """
    filled = matrix.fillna(0)
    column_totals = filled.abs().sum(axis=0)
    normalized = filled.div(column_totals, axis=1).fillna(0)
    return normalized


def compute_indicator_impact_scores(
    normalized_matrix: pd.DataFrame,
) -> dict[str, float]:
    """Collapse the normalized association matrix into a single
    cumulative "event bonus" score per indicator.

    Returns
    -------
    dict mapping indicator_code -> normalized cumulative impact score.
    """
    scores = normalized_matrix.sum(axis=0)
    return scores.to_dict()


def get_event_bonus(
    impact_scores: dict[str, float], indicator_code: str, default: float = 0.0
) -> float:
    """Look up the cumulative event-driven bonus for one indicator.

    Falls back to ``default`` (0.0, i.e. no adjustment) if the
    indicator has no modeled impact links, rather than raising.
    """
    return impact_scores.get(indicator_code, default)


def validate_against_history(
    predicted_change: float,
    observed_change: float,
    tolerance_pp: float = 5.0,
) -> bool:
    """Sanity-check an estimated event impact against what actually
    happened historically (e.g. Telebirr's launch vs. the observed
    mobile-money growth from 4.7% (2021) to 9.45% (2024)).

    Returns True if the predicted change is within ``tolerance_pp``
    percentage points of the observed change.
    """
    return abs(predicted_change - observed_change) <= tolerance_pp
