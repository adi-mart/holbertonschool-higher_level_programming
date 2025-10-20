-- Description: Counts the number of rows with id 89 in first_table.
-- Usage: cat 8-count_89.sql | mysql -hlocalhost -uroot -p [database_name]

SELECT COUNT(*)
FROM first_table
WHERE id = 89;
