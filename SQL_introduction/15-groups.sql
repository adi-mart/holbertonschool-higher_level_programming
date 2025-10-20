-- Description: Shows the number of rows per score in second_table.
-- Usage: cat 15-groups.sql | mysql -hlocalhost -uroot -p [database_name]

SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
