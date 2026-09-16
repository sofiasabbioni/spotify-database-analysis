from pathlib import Path

import pandas as pd

NUMERIC_COLUMNS = [
    "artist_count",
    "released_year",
    "released_month",
    "released_day",
    "in_spotify_playlists",
    "in_spotify_charts",
    "streams",
    "in_apple_playlists",
    "in_apple_charts",
    "in_deezer_playlists",
    "in_deezer_charts",
    "in_shazam_charts",
    "bpm",
    "danceability_%",
    "valence_%",
    "energy_%",
    "acousticness_%",
    "instrumentalness_%",
    "liveness_%",
    "speechiness_%",
]


def parse_artists(value):
    """Split the dataset's comma-separated artist field into clean artist names."""
    if pd.isna(value):
        return []
    return [name.strip() for name in str(value).split(",") if name.strip()]


def load_and_clean_data(path: Path) -> pd.DataFrame:
    """Load the source CSV and clean values before database insertion.

    Numeric strings may contain commas or malformed values. Invalid numeric values
    are coerced to NaN and later inserted as SQL NULL instead of crashing the load.
    """
    data = pd.read_csv(path)

    for column in NUMERIC_COLUMNS:
        cleaned = data[column].astype("string").str.replace(",", "", regex=False).str.strip()
        data[column] = pd.to_numeric(cleaned, errors="coerce")

    data["release_date"] = pd.to_datetime(
        {
            "year": data["released_year"],
            "month": data["released_month"],
            "day": data["released_day"],
        },
        errors="coerce",
    )

    return data


def db_value(value):
    """Convert pandas missing values and NumPy scalars into DB-friendly values."""
    if pd.isna(value):
        return None
    return value.item() if hasattr(value, "item") else value
