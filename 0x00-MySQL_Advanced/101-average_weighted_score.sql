-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE userCount INT;
    DECLARE userId INT;
    DECLARE total_weight INT;
    DECLARE total_weighted_score FLOAT;

    -- Cursor to loop through each user
    DECLARE user_cursor CURSOR FOR SELECT id FROM users;

    -- Declare the CONTINUE handler
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET userCount = 0;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through each user
    user_loop: LOOP
        FETCH user_cursor INTO userId;

        IF userCount = 0 THEN
            LEAVE user_loop;
        END IF;

        -- Calculate total weight
        SELECT SUM(p.weight) INTO total_weight
        FROM projects p
        JOIN corrections c ON p.id = c.project_id
        WHERE c.user_id = userId;

        -- Calculate total weighted score
        SELECT SUM(c.score * p.weight) INTO total_weighted_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = userId;

        -- Update average score in users table
        IF total_weight > 0 THEN
            UPDATE users 
            SET average_score = total_weighted_score / total_weight 
            WHERE id = userId;
        ELSE
            UPDATE users 
            SET average_score = 0 
            WHERE id = userId;
        END IF;
    END LOOP;

    -- Close the cursor
    CLOSE user_cursor;
END //

DELIMITER ;

