-- Description: Creates the first_table table in the current database.
-- Usage: cat 4-first_table.sql | mysql -hlocalhost -uroot -p [database_name]

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
