-- Affiche tous les genres du show 'Dexter'. Trie par nom de genre, une seule requête SELECT.
SELECT genres.name FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN hbtn_0d_tvshows.genres ON tv_show_genres.genre_id = genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY genres.name ASC;
