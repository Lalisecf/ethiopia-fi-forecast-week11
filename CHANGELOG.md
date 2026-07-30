# Changelog — Week 12 Capstone Enhancement

## Final Submission (this update)
- Marked all Week 12 engineering deliverables as complete in the README status table.
- Confirmed SHAP-based explainability module (`src/explainability.py`) is wired to the
  event–indicator association matrix and produces global feature-importance rankings.
- Confirmed the four-page Streamlit dashboard (Overview, Trends, Forecasts, Projections)
  is feature-complete and reads directly from the versioned `reports/` outputs.
- Finalized the technical report / blog post for a finance-sector audience.
- General repository cleanup ahead of final grading (removed stray cache artifacts,
  verified `requirements.txt`, confirmed CI badge renders on `main`).

## Second Interim (previous update)
- Refactored the Week 11 notebook logic into a modular, typed `src/` package
  (`config.py`, `data_loader.py`, `event_model.py`, `forecast.py`, `explainability.py`).
- Added 24 pytest unit/integration tests with shared fixtures (`tests/conftest.py`).
- Configured GitHub Actions CI (flake8 + pytest across Python 3.10/3.11) and added the
  build badge to the README.
- Rewrote the README with business problem, solution overview, project structure, and
  setup instructions.

## First Interim
- Selected the Week 11 "Forecasting Financial Inclusion in Ethiopia" project as the
  Week 12 capstone base and completed the gap analysis / improvement plan.
