-- Updates score of Bob to 10
-- Only use name field

SELECT score, name FROM second_table WHERE name="Bob";
UPDATE second_table SET score=10 WHERE name='Bob';