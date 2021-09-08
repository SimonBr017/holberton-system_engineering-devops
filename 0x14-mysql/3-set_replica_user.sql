-- set up a replica_user

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'C3s2l"m3r2';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
