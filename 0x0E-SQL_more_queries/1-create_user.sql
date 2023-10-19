-- Script: 1-create_user.sql
-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEDGES ON *.* TO 'user_0d_1'@'localhost';
