-- task 6
-- create database
CREATE DATABASE IF NOT EXISTS 'hbtn_0d_usa';
CREATE TABLE IF NOT EXISTS 'hbtn_0d_usa'.'states' (
	id INT UNIQUE PRIMARY KEY AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL
);
