# Write your MySQL query statement below
SELECT user_id AS buyer_id, join_date, 
        COUNT(order_id) AS orders_in_2019 
FROM Users LEFT JOIN Orders  
ON YEAR(order_date) = 2019 AND user_id = buyer_id GROUP BY 1