CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE DATABASE IF NOT EXISTS performance_schema;

USE hbnb_dev_db;
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'%';
FLUSH PRIVILEGES;

USE performance_schema;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'%';
FLUSH PRIVILEGES;
