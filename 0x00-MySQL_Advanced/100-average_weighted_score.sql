-- -- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE weighted_avrg_score FLOAT;
    SET weighted_avrg_score = (SELECT SUM(score * weight) / SUM(weight) FROM users AS U
        JOIN corrections AS C ON U.id = C.user_id
        JOIN projects AS P ON C.project_id = P.id
        WHERE U.id = user_id);
    UPDATE users SET average_weighted_score = weighted_avrg_score WHERE id = user_id;
END$$
DELIMITER ;