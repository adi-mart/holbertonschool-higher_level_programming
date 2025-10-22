-- Crée la table 'unique_id' avec 'id' unique et par défaut à 1, et 'name'. Ne plante pas si la table existe déjà.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
