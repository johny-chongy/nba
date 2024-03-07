CREATE DATABASE nba;

--TABLE teams
    -- id (primary key)
    -- full_name
    -- conference
    -- division
    -- arena

CREATE TABLE teams (
  id VARCHAR(3) PRIMARY KEY,
  full_name VARCHAR(25),
  conference VARCHAR(1),
  division VARCHAR(5),
  arena VARCHAR(50)
);



