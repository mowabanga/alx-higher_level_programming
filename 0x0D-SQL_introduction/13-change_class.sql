-- Removes all records where score <= 5 in second_table
SELECT score, name FROM second_table ORDER BY score DESC;
DELETE FROM second_table WHERE score <= 5;