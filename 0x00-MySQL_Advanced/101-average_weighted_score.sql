-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS US,
    (SELECT U.id, SUM(score * weight) / SUM(weight) AS weighted_avrg
    FROM users AS U
    JOIN corrections AS C ON U.id = C.user_id
    JOIN projects AS P ON C.project_id = P.id
    GROUP BY U.id) AS WA
    SET US.average_score = WA.weighted_avrg
    WHERE US.id = WA.id;
END$$
DELIMITER ;