# Write your MySQL query statement below
SELECT employee_id FROM (SELECT * FROM Salaries UNION ALL SELECT * FROM Employees) AS SE GROUP BY employee_id HAVING COUNT(*) = 1 ORDER BY employee_id ASC