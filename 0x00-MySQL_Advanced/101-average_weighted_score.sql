-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS US,
    (SELECT U.id, SUM(score * weight) / SUM(weight) AS weighted_avrg
    FROM users AS US
    JOIN corrections AS C ON US.id = C.user_id
    JOIN projects AS P ON C.project_id = P.id
    GROUP BY US.id) AS WAV
    SET US.average_score = WAV.weighted_avrg
    WHERE US.id = WAV.id;
END$$
DELIMITER ;