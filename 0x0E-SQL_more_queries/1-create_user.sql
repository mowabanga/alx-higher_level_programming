-- creates user_0d_1
-- Check if the user already exists
SELECT COUNT(*) INTO @user_exists
FROM mysql.user
WHERE user = 'user_0d_1' AND host = '%';

-- If the user does not exist, create it
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
    GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
    SELECT 'User user_0d_1 created and granted all privileges.';
ELSE
    SELECT 'User user_0d_1 already exists. No action taken.';
END IF;
