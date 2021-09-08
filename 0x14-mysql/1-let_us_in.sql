-- creates the MySQL server user to holberton_user usage  cat 1-let_us_in.sql | mysql -hlocalhost -uroot -p

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON * . * TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
