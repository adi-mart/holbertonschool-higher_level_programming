-- Crée la base 'hbtn_0d_2' et l'utilisateur 'user_0d_2' avec le droit SELECT uniquement. Définit le mot de passe et ne plante pas si la base ou l'utilisateur existe déjà.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
