-- Affiche tous les shows sans genre associé (genre_id = NULL). Affiche le titre et l'id du genre, triés par titre et genre.
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
