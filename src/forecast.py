"""
Trend + event-augmented forecasting for Access and Usage indicators.

Refactored out of ``notebooks/task4_forecasting.ipynb``. Wraps the
linear-trend model, confidence intervals, event adjustment, and
scenario generation in typed, independently-testable functions.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

from .config import ForecastConfig


@dataclass
class TrendModelResult:
    """Container for a fitted trend model and its evaluation metrics."""

    model: LinearRegression
    r2: float
    rmse: float
    residual_std: float


def fit_trend_model(series: pd.DataFrame) -> TrendModelResult:
    """Fit a simple linear trend model of ``value_numeric`` on ``year``.

    Parameters
    ----------
    series:
        Output of :func:`src.data_loader.get_indicator_series`, i.e. a
        dataframe with ``year`` and ``value_numeric`` columns.
    """
    x = series[["year"]]
    y = series["value_numeric"]

    model = LinearRegression()
    model.fit(x, y)

    predictions = model.predict(x)
    residuals = y - predictions

    return TrendModelResult(
        model=model,
        r2=r2_score(y, predictions),
        rmse=float(np.sqrt(mean_squared_error(y, predictions))),
        residual_std=float(residuals.std()),
    )


def forecast_trend(
    result: TrendModelResult, years: tuple[int, ...]
) -> pd.DataFrame:
    """Project the fitted trend model forward over ``years``."""
    future = pd.DataFrame({"year": years})
    future["forecast"] = result.model.predict(future[["year"]])
    return future


def add_confidence_interval(
    future: pd.DataFrame,
    residual_std: float,
    config: ForecastConfig,
    base_col: str = "forecast",
) -> pd.DataFrame:
    """Add ``lower``/``upper`` 95% confidence bounds around
    ``base_col`` using the model's residual standard deviation.
    """
    future = future.copy()
    margin = config.confidence_z_score * residual_std
    future["lower"] = future[base_col] - margin
    future["upper"] = future[base_col] + margin
    return future


def apply_event_adjustment(
    future: pd.DataFrame, event_bonus: float, base_col: str = "forecast"
) -> pd.DataFrame:
    """Add a cumulative event-driven bonus to the baseline trend
    forecast, producing an ``event_forecast`` column.
    """
    future = future.copy()
    future["event_forecast"] = future[base_col] + event_bonus
    return future


def add_scenarios(
    future: pd.DataFrame,
    config: ForecastConfig,
    band_pp: float,
    base_col: str = "event_forecast",
) -> pd.DataFrame:
    """Add ``optimistic`` / ``base`` / ``pessimistic`` scenario
    columns around ``base_col`` using a fixed +/- percentage-point band.
    """
    future = future.copy()
    future["base"] = future[base_col]
    future["optimistic"] = future[base_col] + band_pp
    future["pessimistic"] = future[base_col] - band_pp
    return future


def build_forecast_table(
    series: pd.DataFrame,
    config: ForecastConfig,
    event_bonus: float = 0.0,
    scenario_band_pp: float = 3.0,
) -> pd.DataFrame:
    """End-to-end pipeline: fit trend -> forecast -> CI -> event
    adjustment -> scenarios, returning one tidy output table.

    This consolidates what was ~20 separate notebook cells in
    ``task4_forecasting.ipynb`` into a single reusable function.
    """
    trend_result = fit_trend_model(series)
    future = forecast_trend(trend_result, config.forecast_years)
    future = add_confidence_interval(future, trend_result.residual_std, config)
    future = apply_event_adjustment(future, event_bonus)
    future = add_scenarios(future, config, scenario_band_pp, base_col="event_forecast")

    future = future[
        [
            "year",
            "forecast",
            "event_forecast",
            "optimistic",
            "base",
            "pessimistic",
            "lower",
            "upper",
        ]
    ].rename(
        columns={
            "year": "Year",
            "forecast": "Baseline",
            "event_forecast": "Event",
            "optimistic": "Optimistic",
            "base": "Base",
            "pessimistic": "Pessimistic",
            "lower": "Lower",
            "upper": "Upper",
        }
    )
    return future
