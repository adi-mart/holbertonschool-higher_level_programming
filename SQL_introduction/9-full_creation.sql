-- Description: Creates the second_table table and inserts multiple rows.
-- Usage: cat 9-full_creation.sql | mysql -hlocalhost -uroot -p [database_name]

CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score)
    VALUES (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
