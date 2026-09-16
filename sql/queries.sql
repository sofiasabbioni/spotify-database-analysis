USE spotify_most_streamed_songs;

-- 1. Most Streamed Tracks
SELECT track_name, stream_count
FROM Track
WHERE stream_count IS NOT NULL
ORDER BY stream_count DESC
LIMIT 10;

-- 2. Most Popular Artists
-- Collaborative tracks give full credit to each credited artist.
SELECT
    a.name,
    SUM(t.stream_count) AS total_streams,
    COUNT(DISTINCT t.track_id) AS track_count
FROM Artist a
JOIN Track_Artist ta ON ta.artist_id = a.artist_id
JOIN Track t ON t.track_id = ta.track_id
WHERE t.stream_count IS NOT NULL
GROUP BY a.artist_id, a.name
ORDER BY total_streams DESC
LIMIT 5;

-- 3. Average Song Characteristics
SELECT
    ROUND(AVG(bpm), 2) AS avg_bpm,
    ROUND(AVG(energy), 2) AS avg_energy,
    ROUND(AVG(danceability), 2) AS avg_danceability
FROM Characteristics;

-- 4. Tracks in the Most Spotify Playlists/Charts
SELECT
    t.track_name,
    COALESCE(pc.in_spotify_playlists, 0) + COALESCE(pc.in_spotify_charts, 0) AS total_appearances
FROM Track t
JOIN Playlist_Chart pc ON pc.track_id = t.track_id
ORDER BY total_appearances DESC
LIMIT 10;

-- 5. Tracks by Release Year
SELECT
    YEAR(release_date) AS release_year,
    COUNT(*) AS track_count
FROM Track
GROUP BY YEAR(release_date)
ORDER BY release_year DESC;

-- 6. Average Energy by Mode
SELECT
    mode,
    ROUND(AVG(energy), 2) AS avg_energy
FROM Characteristics
WHERE mode IS NOT NULL
GROUP BY mode
ORDER BY mode;

-- 7. Most Danceable Tracks
SELECT
    t.track_name,
    c.danceability
FROM Track t
JOIN Characteristics c ON c.track_id = t.track_id
ORDER BY c.danceability DESC, t.track_name
LIMIT 5;

-- 8. Tracks with the Highest Valence
SELECT
    t.track_name,
    c.valence
FROM Track t
JOIN Characteristics c ON c.track_id = t.track_id
ORDER BY c.valence DESC, t.track_name
LIMIT 5;

-- 9. Most Streamed Collaborative Tracks
-- Refined from the original academic query: a track has one stream count,
-- so the portfolio version reports that count rather than a misleading average.
SELECT
    t.track_name,
    COUNT(ta.artist_id) AS artist_count,
    t.stream_count
FROM Track t
JOIN Track_Artist ta ON ta.track_id = t.track_id
WHERE t.stream_count IS NOT NULL
GROUP BY t.track_id, t.track_name, t.stream_count
HAVING COUNT(ta.artist_id) > 1
ORDER BY t.stream_count DESC
LIMIT 5;
