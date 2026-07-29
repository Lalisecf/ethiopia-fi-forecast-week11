"""
File utility functions.
"""

from pathlib import Path

import pandas as pd


def ensure_directory(path: Path) -> None:
    """
    Create directory if it does not exist.
    """

    path.mkdir(parents=True, exist_ok=True)


def save_csv(
    dataframe: pd.DataFrame,
    output_path: Path
) -> None:
    """
    Save DataFrame to CSV.
    """

    ensure_directory(output_path.parent)

    dataframe.to_csv(output_path, index=False)


def read_csv(file_path: Path) -> pd.DataFrame:
    """
    Read CSV file.
    """

    return pd.read_csv(file_path)