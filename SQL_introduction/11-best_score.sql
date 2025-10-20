-- Description: Lists scores >= 10 from second_table.
-- Usage: cat 11-best_score.sql | mysql -hlocalhost -uroot -p [database_name]

SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
