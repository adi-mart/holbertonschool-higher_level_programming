-- Affiche tous les shows et tous les genres associés (NULL si pas de genre). Trie par titre et nom de genre, une seule requête SELECT.
SELECT tv_shows.title, genres.name FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN hbtn_0d_tvshows.genres ON tv_show_genres.genre_id = genres.id
ORDER BY tv_shows.title ASC, genres.name ASC;
