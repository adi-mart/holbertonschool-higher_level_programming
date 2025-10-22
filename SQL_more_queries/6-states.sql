-- Crée la base 'hbtn_0d_usa' et la table 'states' avec clé primaire et nom non NULL. Ne plante pas si la base ou la table existe déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY KEY UNIQUE NOT NULL,
    name VARCHAR(256)
);
