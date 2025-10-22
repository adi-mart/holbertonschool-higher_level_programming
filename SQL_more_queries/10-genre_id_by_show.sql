-- Affiche tous les shows ayant au moins un genre associé. Affiche le titre et l'id du genre, triés par titre et genre.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM hbtn_0d_tvshows.tv_shows
JOIN hbtn_0d_tvshows.tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
