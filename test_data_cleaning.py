import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from data_utils import load_and_clean_data, parse_artists


class DataCleaningTests(unittest.TestCase):
    def test_parse_multiple_artists(self):
        self.assertEqual(parse_artists("The Weeknd, Madonna, Playboi Carti"),
                         ["The Weeknd", "Madonna", "Playboi Carti"])

    def test_dataset_loads_and_preserves_953_rows(self):
        data = load_and_clean_data(ROOT / "data" / "spotify_most_streamed_songs.csv")
        self.assertEqual(len(data), 953)

    def test_malformed_stream_value_becomes_null(self):
        data = load_and_clean_data(ROOT / "data" / "spotify_most_streamed_songs.csv")
        bad_row = data.loc[data["track_name"] == "Love Grows (Where My Rosemary Goes)", "streams"]
        self.assertEqual(len(bad_row), 1)
        self.assertTrue(bad_row.isna().iloc[0])

    def test_release_year_range(self):
        data = load_and_clean_data(ROOT / "data" / "spotify_most_streamed_songs.csv")
        self.assertEqual(int(data["released_year"].min()), 1930)
        self.assertEqual(int(data["released_year"].max()), 2023)


if __name__ == "__main__":
    unittest.main()
