-- Description: Lists scores and names from second_table in descending order.
-- Usage: cat 10-top_score.sql | mysql -hlocalhost -uroot -p [database_name]

SELECT score, name FROM second_table
ORDER BY score DESC;
