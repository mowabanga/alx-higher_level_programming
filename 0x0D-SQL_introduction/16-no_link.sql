-- lists all records of second_table
SELECT * FROM second_table WHERE name IS NOT NULL AND name <> '' ORDER BY score DESC;