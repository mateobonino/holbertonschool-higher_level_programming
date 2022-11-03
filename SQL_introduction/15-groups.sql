-- task 15
-- number of records
SELECT score, COUNT(*) AS 'number' FROM second_table
GROUP BY score DESC
ORDER BY 'number' DESC
