-- Affiche toutes les villes avec leur état dans la base 'hbtn_0d_usa'. Utilise JOIN et trie par id de ville.
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;