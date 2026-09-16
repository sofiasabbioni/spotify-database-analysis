from pathlib import Path

from data_utils import db_value, load_and_clean_data, parse_artists
from db import get_connection

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "spotify_most_streamed_songs.csv"


def upsert_artist(cursor, artist_name):
    cursor.execute(
        """
        INSERT INTO Artist (name)
        VALUES (%s)
        ON DUPLICATE KEY UPDATE artist_id = LAST_INSERT_ID(artist_id), name = VALUES(name)
        """,
        (artist_name,),
    )
    return cursor.lastrowid


def load_database():
    data = load_and_clean_data(DATA_PATH)
    invalid_streams = int(data["streams"].isna().sum())

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            for source_index, row in data.iterrows():
                track_id = int(source_index) + 1
                release_date = None if row["release_date"] is None else db_value(row["release_date"])
                if release_date is not None:
                    release_date = release_date.date()

                cursor.execute(
                    """
                    INSERT INTO Track (track_id, track_name, release_date, stream_count)
                    VALUES (%s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        track_name = VALUES(track_name),
                        release_date = VALUES(release_date),
                        stream_count = VALUES(stream_count)
                    """,
                    (
                        track_id,
                        row["track_name"],
                        release_date,
                        db_value(row["streams"]),
                    ),
                )

                # Rebuild artist mappings for idempotent reruns.
                cursor.execute("DELETE FROM Track_Artist WHERE track_id = %s", (track_id,))
                for artist_name in parse_artists(row["artist(s)_name"]):
                    artist_id = upsert_artist(cursor, artist_name)
                    cursor.execute(
                        "INSERT IGNORE INTO Track_Artist (track_id, artist_id) VALUES (%s, %s)",
                        (track_id, artist_id),
                    )

                cursor.execute(
                    """
                    INSERT INTO Characteristics (
                        track_id, bpm, musical_key, mode, danceability, valence, energy,
                        acousticness, instrumentalness, liveness, speechiness, cover_url
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        bpm = VALUES(bpm),
                        musical_key = VALUES(musical_key),
                        mode = VALUES(mode),
                        danceability = VALUES(danceability),
                        valence = VALUES(valence),
                        energy = VALUES(energy),
                        acousticness = VALUES(acousticness),
                        instrumentalness = VALUES(instrumentalness),
                        liveness = VALUES(liveness),
                        speechiness = VALUES(speechiness),
                        cover_url = VALUES(cover_url)
                    """,
                    (
                        track_id,
                        db_value(row["bpm"]),
                        db_value(row["key"]),
                        db_value(row["mode"]),
                        db_value(row["danceability_%"]),
                        db_value(row["valence_%"]),
                        db_value(row["energy_%"]),
                        db_value(row["acousticness_%"]),
                        db_value(row["instrumentalness_%"]),
                        db_value(row["liveness_%"]),
                        db_value(row["speechiness_%"]),
                        db_value(row["cover_url"]),
                    ),
                )

                cursor.execute(
                    """
                    INSERT INTO Playlist_Chart (
                        track_id, in_spotify_playlists, in_spotify_charts,
                        in_apple_playlists, in_apple_charts,
                        in_deezer_playlists, in_deezer_charts, in_shazam_charts
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                        in_spotify_playlists = VALUES(in_spotify_playlists),
                        in_spotify_charts = VALUES(in_spotify_charts),
                        in_apple_playlists = VALUES(in_apple_playlists),
                        in_apple_charts = VALUES(in_apple_charts),
                        in_deezer_playlists = VALUES(in_deezer_playlists),
                        in_deezer_charts = VALUES(in_deezer_charts),
                        in_shazam_charts = VALUES(in_shazam_charts)
                    """,
                    (
                        track_id,
                        db_value(row["in_spotify_playlists"]),
                        db_value(row["in_spotify_charts"]),
                        db_value(row["in_apple_playlists"]),
                        db_value(row["in_apple_charts"]),
                        db_value(row["in_deezer_playlists"]),
                        db_value(row["in_deezer_charts"]),
                        db_value(row["in_shazam_charts"]),
                    ),
                )

        connection.commit()
        print(f"Loaded {len(data)} tracks successfully.")
        if invalid_streams:
            print(
                f"Note: {invalid_streams} malformed/missing stream value(s) were stored as NULL "
                "instead of failing the import."
            )
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


if __name__ == "__main__":
    load_database()
