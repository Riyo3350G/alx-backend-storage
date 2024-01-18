-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student.
-- Note: An average score can be a decimal
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score FLOAT;
    SET average_score = (SELECT AVG(score) FROM corrections WHERE user_id = user_id);
    INSERT INTO average_scores (user_id, average_score) VALUES (user_id, average_score);
END$$
DELIMITER ;