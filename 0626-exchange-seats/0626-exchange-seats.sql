# Write your MySQL query statement below
#SELECT id+1 AS id, student FROM Seat WHERE id & 1
#UNION
#SELECT id-1 AS id, student FROM Seat WHERE (id-1) & 1 ORDER BY id
#SELECT (CASE WHEN s1.id % 2 = 1 THEN s2.id ELSE s1.id END), (CASE WHEN s1.id % 2 = 1 THEN s2.student ELSE s1.student END) AS st FROM Seat s1 JOIN Seat s2 ON s2.id - s1.id = 1

SELECT s1.id AS id, IFNULL(s2.student, s1.student) AS student FROM (SELECT * FROM Seat WHERE id & 1) s1 LEFT JOIN Seat s2 ON s2.id - s1.id = 1
UNION
SELECT s2.id AS id, s1.student AS student FROM (SELECT * FROM Seat WHERE (id+1)&1 ) s2 JOIN Seat s1 ON s2.id - s1.id = 1 ORDER BY 1
#SELECT id-1 AS id, student FROM Seat WHERE (id-1) & 1 ORDER BY 1