" SQL Introduction Project
" 
" This project consists of a series of SQL scripts that demonstrate various SQL operations on a MySQL server. The scripts are designed to perform tasks such as creating databases, creating and managing tables, inserting and retrieving data, and performing SQL queries.
" 
" Task 0: List Databases
" 
" - **Script File**: [0-list_databases.sql](0x0D-SQL_introduction/0-list_databases.sql)
" - **Description**: This script lists all databases on the MySQL server.
" 
" Task 1: Create a Database
" 
" - **Script File**: [1-create_database_if_missing.sql](0x0D-SQL_introduction/1-create_database_if_missing.sql)
" - **Description**: This script creates the database "hbtn_0c_0" on the MySQL server if it doesn't already exist.
" 
" Task 2: Delete a Database
" 
" - **Script File**: [2-remove_database.sql](0x0D-SQL_introduction/2-remove_database.sql)
" - **Description**: This script deletes the "hbtn_0c_0" database on the MySQL server if it exists.
" 
" Task 3: List Tables
" 
" - **Script File**: [3-list_tables.sql](0x0D-SQL_introduction/3-list_tables.sql)
" - **Description**: This script lists all tables in a specified database.
" 
" Task 4: Create a Table
" 
" - **Script File**: [4-first_table.sql](0x0D-SQL_introduction/4-first_table.sql)
" - **Description**: This script creates a table named "first_table" with columns "id" and "name" in a specified database.
" 
" Task 5: Full Table Description
" 
" - **Script File**: [5-full_table.sql](0x0D-SQL_introduction/5-full_table.sql)
" - **Description**: This script prints the full description of the "first_table" in the specified database.
" 
" Task 6: List All Table Rows
" 
" - **Script File**: [6-list_values.sql](0x0D-SQL_introduction/6-list_values.sql)
" - **Description**: This script lists all rows in the "first_table" of the specified database.
" 
" Task 7: Insert a New Row
" 
" - **Script File**: [7-insert_value.sql](0x0D-SQL_introduction/7-insert_value.sql)
" - **Description**: This script inserts a new row into the "first_table" of the specified database.
" 
" Task 8: Count Rows with id = 89
" 
" - **Script File**: [8-count_89.sql](0x0D-SQL_introduction/8-count_89.sql)
" - **Description**: This script counts the number of records with id = 89 in the "first_table" of the specified database.
" 
" Task 9: Create a Table with Multiple Rows
" 
" - **Script File**: [9-full_creation.sql](0x0D-SQL_introduction/9-full_creation.sql)
" - **Description**: This script creates a table named "second_table" with columns "id," "name," and "score" in the specified database, and adds multiple rows.
" 
" Task 10: List Records by Score
" 
" - **Script File**: [10-top_score.sql](0x0D-SQL_introduction/10-top_score.sql)
" - **Description**: This script lists records in the "second_table" of the specified database, ordered by score.
" 
" ...
" (Include information for the remaining tasks)
" 
" Getting Started
" 
" Before running these scripts, ensure that you have MySQL installed and set up on your system. You will also need the necessary permissions and credentials to connect to the MySQL server.
" 
" Running the Scripts
" 
" To run the scripts, use the following command format:
" 
" ```bash
" cat script.sql | mysql -hlocalhost -uroot -p [database_name]
" ```
" 
" Replace `[database_name]` with the name of the target database.
