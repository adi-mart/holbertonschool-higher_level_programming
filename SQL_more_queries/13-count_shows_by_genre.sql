-- Affiche chaque genre et le nombre de shows associés. Trie par nombre de shows décroissant, n'affiche pas les genres sans show.
SELECT genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_show_genres
JOIN genres ON tv_show_genres.genre_id = genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
