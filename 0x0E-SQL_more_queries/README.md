**0x0E. SQL - More queries**

In this project, we will write SQL scripts to perform various tasks using a sample database. Below are the tasks and SQL scripts that need to be created.

**Task 0: My privileges!**
**Script: 0-privileges.sql**

This script lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

**Task 1: Root user**
**Script: 1-create_user.sql**

This script creates the MySQL server user user_0d_1 with all privileges on your MySQL server. The password for user_0d_1 is set to user_0d_1_pwd.

**Task 2: Read user**
**Script: 2-create_read_user.sql**

This script creates the database hbtn_0d_2 and the user user_0d_2. user_0d_2 is given only SELECT privilege in the database hbtn_0d_2, and the password for user_0d_2 is set to user_0d_2_pwd.

**Task 3: Always a name**
**Script: 3-force_name.sql**

This script creates a table force_name with columns id and name on your MySQL server. The name column is set to be NOT NULL.

**Task 4: ID can't be null**
**Script: 4-never_empty.sql**

This script creates a table id_not_null with columns id (with a default value of 1) and name on your MySQL server.

**Task 5: Unique ID**
**Script: 5-unique_id.sql**

This script creates a table unique_id with columns id (with a default value of 1) and name on your MySQL server. The id column is set to be unique.

**Task 6: States table**
**Script: 6-states.sql**

This script creates the database hbtn_0d_usa and the table states in the database. The states table has columns id (unique, auto-generated), and name (NOT NULL).

**Task 7: Cities table**
**Script: 7-cities.sql**

This script creates the database hbtn_0d_usa and the table cities in the database. The cities table has columns id (unique, auto-generated), state_id (FOREIGN KEY to states), and name (NOT NULL).

**Task 8: Cities of California**
**Script: 8-cities_of_california_subquery.sql**

This script lists all the cities of California that can be found in the database hbtn_0d_usa. It retrieves the data without using the JOIN keyword.

**Task 9: Cities by States**
**Script: 9-cities_by_state_join.sql**

This script lists all cities contained in the database hbtn_0d_usa. Each record displays cities.id, cities.name, and states.name. It retrieves the data using a JOIN statement.

**Task 10: Genre ID by show**
**Script: 10-genre_id_by_show.sql**

This script lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. Each record displays tv_shows.title and tv_show_genres.genre_id.

**Task 11: Genre ID for all shows**
**Script: 11-genre_id_all_shows.sql**

This script lists all shows contained in the database hbtn_0d_tvshows. Each record displays tv_shows.title and tv_show_genres.genre_id. It shows NULL if a show doesn't have a genre linked.

**Task 12: No genre**
**Script: 12-no_genre.sql**

This script lists all shows contained in hbtn_0d_tvshows without a genre linked. Each record displays tv_shows.title and tv_show_genres.genre_id.

**Task 13: Number of shows by genre**
**Script: 13-count_shows_by_genre.sql**

This script lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each genre. Each record displays genre and number_of_shows.

**Task 14: My genres**
**Script: 14-my_genres.sql**

This script lists all genres of the show Dexter in the database hbtn_0d_tvshows. It displays each genre's name.

**Task 15: Only Comedy**
**Script: 15-comedy_only.sql**

