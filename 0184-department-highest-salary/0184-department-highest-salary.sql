# Write your MySQL query statement below
SELECT d.name AS Department, e.name AS Employee, salary AS Salary FROM (SELECT e1.departmentId, e1.name, e1.salary FROM Employee e1 JOIN (SELECT departmentId, MAX(salary) AS salary FROM Employee GROUP BY departmentId) e2 ON e1.departmentId = e2.departmentId AND e1.salary = e2.salary) e JOIN Department d ON e.departmentId = d.id
#SELECT departmentId, e.Salary FROM Employee GROUP BY departmentId
#FROM (SELECT d.name AS dname, e.name AS ename, e.salary FROM Employee e JOIN Department d ON e.departmentId = d.id) e JOIN Employee e2 ON e2.departmentId =
