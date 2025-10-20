-- Description: Lists rows from second_table where the name is not NULL.
-- Usage: cat 16-no_link.sql | mysql -hlocalhost -uroot -p [database_name]

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

