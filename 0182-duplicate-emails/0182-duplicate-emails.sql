# Write your MySQL query statement below
SELECT email AS Email FROM Person GROUP BY 1 HAVING COUNT(1)> 1