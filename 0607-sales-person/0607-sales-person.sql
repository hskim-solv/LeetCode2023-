# Write your MySQL query statement below

SELECT name FROM SalesPerson s WHERE sales_id NOT IN (SELECT DISTINCT sales_id FROM Orders JOIN (SELECT com_id, name FROM Company WHERE name = "RED") c USING(com_id) )