-- Create database and user with privileges on said database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
