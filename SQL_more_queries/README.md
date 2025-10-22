# SQL - More Queries

This project contains SQL scripts for advanced database operations including user management, table creation with constraints, and complex queries with joins.

## Directory Structure

```
SQL_more_queries/
├── 0-privileges.sql
├── 1-create_user.sql
├── 2-create_read_user.sql
├── 3-force_name.sql
├── 4-never_empty.sql
├── 5-unique_id.sql
├── 6-states.sql
├── 7-cities.sql
├── 8-cities_of_california_subquery.sql
├── 9-cities_by_state_join.sql
├── 10-genre_id_by_show.sql
├── 11-genre_id_all_shows.sql
├── 12-no_genre.sql
├── 13-count_shows_by_genre.sql
├── 14-my_genres.sql
├── 15-comedy_only.sql
├── 16-shows_by_genre.sql
└── README.md
```

## Description

This project covers advanced SQL concepts such as:
- Creating and managing MySQL users and privileges
- Creating tables with constraints (NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY)
- Using subqueries and different types of joins
- Counting and grouping data
- Working with multiple tables and databases

## Files Description

| File | Description |
|------|-------------|
| `0-privileges.sql` | Shows privileges for specific MySQL users |
| `1-create_user.sql` | Creates a MySQL user with all privileges |
| `2-create_read_user.sql` | Creates a database and a user with SELECT privilege only |
| `3-force_name.sql` | Creates a table with a NOT NULL constraint |
| `4-never_empty.sql` | Creates a table with a DEFAULT value |
| `5-unique_id.sql` | Creates a table with a UNIQUE constraint |
| `6-states.sql` | Creates a database and states table with PRIMARY KEY |
| `7-cities.sql` | Creates a cities table with FOREIGN KEY constraint |
| `8-cities_of_california_subquery.sql` | Lists California cities using subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their states using JOIN |
| `10-genre_id_by_show.sql` | Lists shows with at least one genre using INNER JOIN |
| `11-genre_id_all_shows.sql` | Lists all shows including those without genres using LEFT JOIN |
| `12-no_genre.sql` | Lists shows without any genre |
| `13-count_shows_by_genre.sql` | Counts shows by genre using GROUP BY and HAVING |
| `14-my_genres.sql` | Lists all genres for a specific show using multiple JOINs |
| `15-comedy_only.sql` | Lists all comedy shows |
| `16-shows_by_genre.sql` | Lists all shows and their genres (including NULL) |

## Usage

Each SQL script can be executed with the MySQL command line:

```bash
cat filename.sql | mysql -hlocalhost -uroot -p [database_name]
```

Example:
```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

## Requirements

- All files are tested on Ubuntu 20.04 LTS using MySQL 8.0
- All SQL keywords are in uppercase
- All files end with a new line
- Each file starts with a comment describing the task

## Author

Project completed as part of the Holberton School Higher Level Programming curriculum.
