from __future__ import annotations

from src.config import ForecastConfig
from src.forecast import (
    add_confidence_interval,
    add_scenarios,
    apply_event_adjustment,
    build_forecast_table,
    fit_trend_model,
    forecast_trend,
)


def test_fit_trend_model_returns_positive_slope_for_growth_data(
    sample_indicator_series,
):
    result = fit_trend_model(sample_indicator_series)
    assert result.model.coef_[0] > 0
    assert 0.0 <= result.r2 <= 1.0
    assert result.rmse >= 0
    assert result.residual_std >= 0


def test_forecast_trend_produces_one_row_per_year(sample_indicator_series):
    result = fit_trend_model(sample_indicator_series)
    future = forecast_trend(result, (2025, 2026, 2027))
    assert list(future["year"]) == [2025, 2026, 2027]
    assert "forecast" in future.columns
    # forecast should continue the upward trend beyond 2024's 49.0
    assert future["forecast"].iloc[-1] > sample_indicator_series["value_numeric"].iloc[-1]


def test_add_confidence_interval_bounds_are_symmetric(sample_indicator_series):
    result = fit_trend_model(sample_indicator_series)
    future = forecast_trend(result, (2025, 2026, 2027))
    config = ForecastConfig()
    future_ci = add_confidence_interval(future, result.residual_std, config)
    midpoint = (future_ci["lower"] + future_ci["upper"]) / 2
    assert (midpoint - future_ci["forecast"]).abs().max() < 1e-6
    assert (future_ci["upper"] >= future_ci["lower"]).all()


def test_apply_event_adjustment_adds_bonus(sample_indicator_series):
    result = fit_trend_model(sample_indicator_series)
    future = forecast_trend(result, (2025, 2026, 2027))
    adjusted = apply_event_adjustment(future, event_bonus=2.0)
    diff = adjusted["event_forecast"] - future["forecast"]
    assert (diff == 2.0).all()


def test_add_scenarios_orders_pessimistic_base_optimistic(sample_indicator_series):
    result = fit_trend_model(sample_indicator_series)
    future = forecast_trend(result, (2025, 2026, 2027))
    adjusted = apply_event_adjustment(future, event_bonus=0.0)
    config = ForecastConfig()
    scenarios = add_scenarios(adjusted, config, band_pp=3.0)
    assert (scenarios["pessimistic"] <= scenarios["base"]).all()
    assert (scenarios["base"] <= scenarios["optimistic"]).all()


def test_build_forecast_table_end_to_end_has_expected_columns(
    sample_indicator_series,
):
    config = ForecastConfig()
    table = build_forecast_table(
        sample_indicator_series, config, event_bonus=1.2, scenario_band_pp=3.0
    )
    expected_columns = {
        "Year",
        "Baseline",
        "Event",
        "Optimistic",
        "Base",
        "Pessimistic",
        "Lower",
        "Upper",
    }
    assert expected_columns.issubset(set(table.columns))
    assert len(table) == len(config.forecast_years)
