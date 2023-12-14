-- Create the stored procedure

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Calculate total score and total projects
    SELECT SUM(score), COUNT(DISTINCT project_id)
    INTO total_score, total_projects
    FROM corrections
    WHERE user_id = p_user_id;

    -- Calculate average score and update the user's record
    IF total_projects > 0 THEN
        UPDATE users
        SET average_score = total_score / total_projects
        WHERE id = p_user_id;
    ELSE
        -- No projects for the user, set average_score to 0
        UPDATE users
        SET average_score = 0
        WHERE id = p_user_id;
    END IF;
END;

