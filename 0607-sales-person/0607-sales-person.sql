# Write your MySQL query statement below

SELECT s.name FROM SalesPerson s WHERE s.sales_id NOT IN (SELECT DISTINCT o.sales_id FROM Orders o JOIN Company c ON c.com_id=o.com_id  AND c.name = "RED")