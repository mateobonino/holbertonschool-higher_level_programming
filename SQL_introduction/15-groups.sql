-- task 15
-- number of records
SELECT score, COUNT(*) number FROM second_table
GROUP BY score
ORDER BY score DESC;
