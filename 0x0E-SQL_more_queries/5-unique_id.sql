-- script that creates the table unique
-- id has default value 1 and unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256));
