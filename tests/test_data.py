import pandas as pd
from pathlib import Path


def test_dataset_exists():
    assert Path("data/raw/ethiopia_fi_unified_data.xlsx").exists()


def test_reference_exists():
    assert Path("data/raw/reference_codes.csv").exists()