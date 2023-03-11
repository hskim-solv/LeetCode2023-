# Write your MySQL query statement below

SELECT s.name FROM SalesPerson s WHERE s.sales_id NOT IN (SELECT DISTINCT sales_id FROM Orders JOIN Company USING(com_id) WHERE name = "RED")