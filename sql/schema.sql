-- Spotify Database Analysis - portfolio schema
-- MySQL 8+

CREATE DATABASE IF NOT EXISTS spotify_most_streamed_songs
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE spotify_most_streamed_songs;

CREATE TABLE IF NOT EXISTS Artist (
    artist_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Track (
    track_id INT PRIMARY KEY,
    track_name VARCHAR(500) NOT NULL,
    release_date DATE NOT NULL,
    stream_count BIGINT NULL
) ENGINE=InnoDB;

-- A track can have multiple artists and an artist can appear on multiple tracks.
CREATE TABLE IF NOT EXISTS Track_Artist (
    track_id INT NOT NULL,
    artist_id INT NOT NULL,
    PRIMARY KEY (track_id, artist_id),
    CONSTRAINT fk_track_artist_track
        FOREIGN KEY (track_id) REFERENCES Track(track_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_track_artist_artist
        FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Characteristics (
    track_id INT PRIMARY KEY,
    bpm INT NULL,
    musical_key VARCHAR(10) NULL,
    mode VARCHAR(10) NULL,
    danceability DECIMAL(5,2) NULL,
    valence DECIMAL(5,2) NULL,
    energy DECIMAL(5,2) NULL,
    acousticness DECIMAL(5,2) NULL,
    instrumentalness DECIMAL(5,2) NULL,
    liveness DECIMAL(5,2) NULL,
    speechiness DECIMAL(5,2) NULL,
    cover_url TEXT NULL,
    CONSTRAINT fk_characteristics_track
        FOREIGN KEY (track_id) REFERENCES Track(track_id)
        ON DELETE CASCADE
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS Playlist_Chart (
    track_id INT PRIMARY KEY,
    in_spotify_playlists INT NULL,
    in_spotify_charts INT NULL,
    in_apple_playlists INT NULL,
    in_apple_charts INT NULL,
    in_deezer_playlists INT NULL,
    in_deezer_charts INT NULL,
    in_shazam_charts INT NULL,
    CONSTRAINT fk_playlist_chart_track
        FOREIGN KEY (track_id) REFERENCES Track(track_id)
        ON DELETE CASCADE
) ENGINE=InnoDB;
