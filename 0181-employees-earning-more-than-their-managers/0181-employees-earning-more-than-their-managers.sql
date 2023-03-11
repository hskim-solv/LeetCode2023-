# Write your MySQL query statement below
SELECT a.name AS Employee FROM Employee a WHERE a.salary >= (SELECT b.salary FROM Employee b WHERE b.id=a.managerId)