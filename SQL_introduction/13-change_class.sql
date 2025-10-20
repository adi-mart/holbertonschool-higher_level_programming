-- Description: Removes rows with score <= 5 from second_table.
-- Usage: cat 13-change_class.sql | mysql -hlocalhost -uroot -p [database_name]

DELETE FROM second_table
WHERE score <= 5;
