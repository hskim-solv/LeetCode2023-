# Write your MySQL query statement below
SELECT u.user_id AS buyer_id, 
        u.join_date, 
        IFNULL(o.orders, 0) AS orders_in_2019 
FROM Users u 
LEFT JOIN 
(SELECT buyer_id, COUNT(order_id) AS orders 
 FROM Orders 
 WHERE YEAR(order_date) = 2019 
 GROUP BY 1) o  
ON o.buyer_id=u.user_id