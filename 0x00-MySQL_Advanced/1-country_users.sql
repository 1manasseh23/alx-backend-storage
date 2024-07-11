-- Drop the existing table if it exists (be cautious with existing data)
DROP TABLE IF EXISTS users;

-- Create the users table with required columns
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
