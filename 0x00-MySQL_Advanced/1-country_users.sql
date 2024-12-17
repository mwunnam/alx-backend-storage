-- SQL script That Creates a table user with enumeration of contries

CREATE TABLE IF NOT EXISTS users (
	id INT PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL,
	country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
