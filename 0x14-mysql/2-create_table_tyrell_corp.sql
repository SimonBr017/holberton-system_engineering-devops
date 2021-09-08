-- create database tyrell_corp, and a table nexus6 with one entry
-- give SELECT permision to holberton_user, usage: cat 2-create_table_tyrell_corp.sql | mysql -hlocalhost -uroot -p

CREATE DATABASE IF NOT EXISTS tyrell_corp;
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (
	id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
INSERT INTO tyrell_corp.nexus6 (name) VALUES ('Leon');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
