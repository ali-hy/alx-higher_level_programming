-- script that creates the table unique_id on your MySQL server
CREATE TABLE IF NOT EXISTS unique_id (
    id INT CONSTRAINT UNIQUE,
    name VARCHAR(256)
);
