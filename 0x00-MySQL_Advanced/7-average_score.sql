-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT DEFAULT 0;
    DECLARE score_count INT DEFAULT 0;
    DECLARE average_score FLOAT;

    -- Calculate total score and count of scores for the user
    SELECT SUM(score), COUNT(score) INTO total_score, score_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate average score
    IF score_count > 0 THEN
        SET average_score = total_score / score_count;
    ELSE
        SET average_score = 0;
    END IF;

    -- Update the user's average score
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END //

DELIMITER ;

