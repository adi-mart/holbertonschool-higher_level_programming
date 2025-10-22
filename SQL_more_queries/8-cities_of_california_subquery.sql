-- Affiche toutes les villes de Californie dans la base 'hbtn_0d_usa'. Utilise une sous-requête, sans JOIN, et trie par id.
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
