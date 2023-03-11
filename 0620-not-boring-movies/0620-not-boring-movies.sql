# Write your MySQL query statement below
SELECT * FROM Cinema WHERE id&1 = TRUE AND description != "boring" ORDER BY rating DESC