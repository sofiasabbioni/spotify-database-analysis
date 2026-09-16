# Sample Results

These values are computed from the included source CSV after applying the same cleaning logic used by the portfolio loader. They are included so the project can be reviewed without a running MySQL instance.

## Query 1 - Most Streamed Tracks

| track_name                                    |    streams |
|:----------------------------------------------|-----------:|
| Blinding Lights                               | 3703895074 |
| Shape of You                                  | 3562543890 |
| Someone You Loved                             | 2887241814 |
| Dance Monkey                                  | 2864791672 |
| Sunflower - Spider-Man: Into the Spider-Verse | 2808096550 |
| One Dance                                     | 2713922350 |
| STAY (with Justin Bieber)                     | 2665343922 |
| Believer                                      | 2594040133 |
| Closer                                        | 2591224264 |
| Starboy                                       | 2565529693 |

## Query 2 - Most Popular Artists

Collaborative tracks give full stream credit to each credited artist.

| artist       |   total_streams |   track_count |
|:-------------|----------------:|--------------:|
| The Weeknd   |  23,929,760,757 |            36 |
| Bad Bunny    |  23,813,527,270 |            40 |
| Ed Sheeran   |  15,316,587,718 |            14 |
| Taylor Swift |  14,630,378,183 |            38 |
| Harry Styles |  11,608,645,649 |            17 |

## Query 3 - Average Song Characteristics

- Average BPM: **122.54**
- Average energy: **64.28**
- Average danceability: **66.97**

## Query 4 - Most Spotify Playlist/Chart Appearances

| track_name                                |   total_appearances |
|:------------------------------------------|--------------------:|
| Get Lucky - Radio Edit                    |               52898 |
| Mr. Brightside                            |               51994 |
| Wake Me Up - Radio Edit                   |               50921 |
| Smells Like Teen Spirit - Remastered 2021 |               50000 |
| Take On Me                                |               44944 |
| Blinding Lights                           |               43968 |
| One Dance                                 |               43281 |
| Somebody That I Used To Know              |               42798 |
| Everybody Wants To Rule The World         |               41776 |
| Sweet Child O' Mine                       |               41232 |

## Query 6 - Average Energy by Mode

| mode   |   energy_% |
|:-------|-----------:|
| Major  |      63.5  |
| Minor  |      65.34 |

## Query 7 - Most Danceable Tracks

| track_name          |   danceability_% |
|:--------------------|-----------------:|
| Peru                |               96 |
| Players             |               95 |
| The Real Slim Shady |               95 |
| CAIRO               |               95 |
| Super Freaky Girl   |               95 |

## Query 8 - Highest Valence Tracks

| track_name                      |   valence_% |
|:--------------------------------|------------:|
| Zona De Perigo                  |          97 |
| Doja                            |          97 |
| There's Nothing Holdin' Me Back |          97 |
| En El Radio Un Cochinero        |          97 |
| JGL                             |          97 |

## Query 9 - Most Streamed Collaborative Tracks

| track_name                                    |   artist_count |    streams |
|:----------------------------------------------|---------------:|-----------:|
| Sunflower - Spider-Man: Into the Spider-Verse |              2 | 2808096550 |
| One Dance                                     |              3 | 2713922350 |
| STAY (with Justin Bieber)                     |              2 | 2665343922 |
| Closer                                        |              2 | 2591224264 |
| Starboy                                       |              2 | 2565529693 |
