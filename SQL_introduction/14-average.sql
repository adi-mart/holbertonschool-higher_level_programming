-- Description: Calculates the average score from second_table.
-- Usage: cat 14-average.sql | mysql -hlocalhost -uroot -p [database_name]

SELECT AVG(score) AS average FROM second_table;
