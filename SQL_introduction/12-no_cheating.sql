-- Description: Updates Bob's score to 10 in second_table.
-- Usage: cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p [database_name]

UPDATE second_table
SET score = 10
WHERE name = "Bob";
