-- create table in current DB
-- if table exists, script should not fail
-- not allowed to use SELECt or SHOW

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);