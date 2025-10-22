-- Crée la table 'force_name' avec une colonne 'name' qui ne peut pas être NULL. Ne plante pas si la table existe déjà.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name  VARCHAR(256) NOT NULL
);
