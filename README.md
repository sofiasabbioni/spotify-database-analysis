# Spotify Database Analysis

Group academic project developed as part of a **Databases and Big Data** course during my Bachelor's degree.

The project designs and analyses a relational database built from a music-streaming dataset containing **953 tracks and 25 attributes**. It combines **MySQL, SQL, Python and Pandas** to transform raw CSV data into a structured database and answer analytical questions about tracks, artists, streaming performance and musical characteristics.

---

## Project Overview

The dataset contains information on:

- track titles and release dates;
- artists and collaborations;
- streaming performance;
- playlist and chart appearances;
- musical characteristics such as BPM, energy, danceability, valence and acousticness.

The project follows an end-to-end database workflow:

1. design the relational schema;
2. clean and transform the raw CSV data;
3. load the data into MySQL;
4. run analytical SQL queries;
5. explore results through a Python query tool.

---

## Key Features

- Relational database design in **MySQL**
- Normalised representation of tracks, artists and collaborations
- Python-based ETL pipeline using **Pandas** and **PyMySQL**
- Defensive cleaning of malformed and missing values
- Many-to-many relationship between tracks and artists
- SQL analysis across multiple related tables
- Nine analytical queries covering streaming performance and musical characteristics
- Environment-based database configuration
- Reproducible project structure suitable for local execution

---

## Database Design

The main schema is organised around five tables:

### `Artist`

Stores unique artist information.

### `Track`

Stores information about individual tracks, including title and release date.

### `Track_Artist`

Implements the many-to-many relationship between tracks and artists, allowing collaborations to be represented correctly.

### `Characteristics`

Stores musical attributes associated with each track, including:

- BPM
- energy
- danceability
- valence
- acousticness
- instrumentalness
- liveness

### `Playlist_Chart`

Stores playlist and chart performance across streaming platforms.

---

## Data Pipeline

The Python loading pipeline prepares the raw CSV before inserting the data into MySQL.

The cleaning process includes:

- safe numeric conversion;
- removal of commas from numeric fields;
- conversion of invalid numeric values to SQL `NULL`;
- reconstruction of release dates from year, month and day;
- normalization of comma-separated artist names;
- insertion of artist-track relationships into `Track_Artist`.

One malformed stream value in the source data is preserved as `NULL` rather than dropping the full track record.

---

## SQL Analysis

The project includes nine analytical queries.

### Query 1 — Most Streamed Tracks

Identifies the tracks with the highest total stream counts.

### Query 2 — Most Popular Artists

Aggregates track streams by artist to identify the highest-streamed artists.

### Query 3 — Average Song Characteristics

Calculates average values for selected musical characteristics such as BPM, energy and danceability.

### Query 4 — Tracks in Multiple Playlists / Charts

Identifies tracks with the strongest playlist and chart presence.

### Query 5 — Tracks by Release Year

Counts the number of tracks released in each year.

### Query 6 — Energy by Musical Mode

Compares average energy between tracks in major and minor modes.

### Query 7 — Most Danceable Tracks

Ranks tracks by danceability score.

### Query 8 — Highest-Valence Tracks

Identifies tracks with the highest valence scores.

### Query 9 — Most Streamed Collaborative Tracks

Identifies highly streamed tracks involving multiple artists.

---

## Technologies

**MySQL** · **SQL** · **Python** · **Pandas** · **PyMySQL**

---

## Repository Structure

```text
spotify-database-analysis/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── data/
│   ├── README.md
│   └── spotify_most_streamed_songs.csv
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── src/
│   ├── db.py
│   ├── data_utils.py
│   ├── data_loader.py
│   └── query_tool.py
│
├── tests/
│   └── test_data_cleaning.py
│
└── docs/
    ├── academic_presentation.pdf
    └── sample_results.md
```

---

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Configure the database connection

Copy `.env.example` and provide your local MySQL credentials.

Example:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=spotify_most_streamed_songs
```

Do not commit real database credentials.

### 3. Create the schema

Run:

```text
sql/schema.sql
```

in MySQL.

### 4. Load the dataset

```bash
python src/data_loader.py
```

### 5. Explore the analytical queries

Run the SQL queries directly from:

```text
sql/queries.sql
```

or use the Python query tool:

```bash
python src/query_tool.py
```

---

## Main Learning Outcomes

This project provided practical experience in:

- relational database modelling;
- entity relationships and normalization;
- SQL joins and aggregations;
- Python-to-MySQL integration;
- ETL and data cleaning;
- analytical querying;
- transforming raw data into a structured database.

---

## Academic Context

This project was developed as a **group academic project** for a Databases and Big Data course during my Bachelor's degree.

It combines **database design, SQL analysis and Python-based data processing** in an end-to-end workflow.

---

## Limitations

- The analysis is based on the supplied academic dataset rather than live streaming-platform data.
- Streaming metrics represent the information contained in the source dataset and should not be interpreted as current values.
- One source record contains a malformed stream value and is retained with a `NULL` stream count.
