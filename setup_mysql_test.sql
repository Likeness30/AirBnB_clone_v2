-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- More configurations Should be added below
