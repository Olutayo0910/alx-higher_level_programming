-- script that creates the table force_name
-- if the table exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name (
	id INT, 
	name VARCHAR(256) NOT NULL);
