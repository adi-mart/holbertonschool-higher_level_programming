-- Affiche chaque genre et le nombre de shows associés. Trie par nombre de shows décroissant, n'affiche pas les genres sans show.
SELECT genres.name AS genre, COUNT(tv_show_genres.tv_show_id) AS number_of_shows
FROM hbtn_0d_tvshows.tv_show_genres
JOIN hbtn_0d_tvshows.genres ON tv_show_genres.genre_id = genres.id
GROUP BY genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
