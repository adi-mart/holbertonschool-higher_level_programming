# SQL_introduction

This directory contains a series of SQL scripts to learn and manipulate MySQL databases as part of the Holberton School curriculum.

## Directory Structure

```
SQL_introduction/
├── 0-list_databases.sql
├── 1-create_database_if_missing.sql
├── 2-remove_database.sql
├── 3-list_tables.sql
├── 4-first_table.sql
├── 5-full_table.sql
├── 6-list_values.sql
├── 7-insert_value.sql
├── 8-count_89.sql
├── 9-full_creation.sql
├── 10-top_score.sql
├── 11-best_score.sql
├── 12-no_cheating.sql
├── 13-change_class.sql
├── 14-average.sql
├── 15-groups.sql
├── 16-no_link.sql
└── README.md
```

## Content

- **0-list_databases.sql**: Lists all databases on the MySQL server
- **1-create_database_if_missing.sql**: Creates the `hbtn_0c_0` database if it does not exist
- **2-remove_database.sql**: Removes the `hbtn_0c_0` database if it exists
- **3-list_tables.sql**: Lists all tables in a given database
- **4-first_table.sql**: Creates the `first_table` table in the current database
- **5-full_table.sql**: Shows the structure of the `first_table` table (without DESCRIBE/EXPLAIN)
- **6-list_values.sql**: Lists all rows from the `first_table` table
- **7-insert_value.sql**: Inserts a row into `first_table`
- **8-count_89.sql**: Counts the number of rows with id 89 in `first_table`
- **9-full_creation.sql**: Creates the `second_table` table and inserts multiple rows
- **10-top_score.sql**: Lists scores and names from `second_table` in descending order
- **11-best_score.sql**: Lists scores >= 10 from `second_table`
- **12-no_cheating.sql**: Updates Bob's score to 10 in `second_table`
- **13-change_class.sql**: Removes rows with score <= 5 from `second_table`
- **14-average.sql**: Calculates the average score from `second_table`
- **15-groups.sql**: Shows the number of rows per score in `second_table`
- **16-no_link.sql**: Lists rows from `second_table` where the name is not NULL

## Usage

To execute a SQL script:

```bash
cat script.sql | mysql -hlocalhost -uroot -p [database_name]
```

Or, if root authentication is via socket:

```bash
sudo mysql -u root [database_name] < script.sql
```

## Constraints
- Do not use `DESCRIBE` or `EXPLAIN` unless specified
- Respect the required file structure and naming

## Author
adi-mart