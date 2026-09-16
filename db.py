import os
from pathlib import Path

import pymysql
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")


def get_connection():
    """Create a MySQL connection using environment variables."""
    return pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "spotify_most_streamed_songs"),
        charset="utf8mb4",
        autocommit=False,
    )
