# Write your MySQL query statement below
#SELECT c.name AS Customers FROM Customers c WHERE c.id NOT IN (SELECT o.customerId FROM Orders o)
SELECT c.name AS Customers FROM Customers c LEFT JOIN Orders o ON (o.customerId = c.id) WHERE o.id IS NULL