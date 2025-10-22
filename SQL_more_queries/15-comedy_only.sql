-- Affiche tous les shows du genre 'Comedy'. Trie par titre, une seule requête SELECT.
SELECT tv_shows.title FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
JOIN hbtn_0d_tvshows.genres ON tv_show_genres.genre_id = genres.id
WHERE genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
