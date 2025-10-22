-- Affiche tous les shows sans genre associé (genre_id = NULL). Affiche le titre et l'id du genre, triés par titre et genre.
SELECT tv_shows.title, tv_show_genres.genre_id FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
