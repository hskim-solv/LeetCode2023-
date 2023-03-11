# Write your MySQL query statement below
SELECT product_id, product_name FROM Product 
WHERE product_id NOT IN 
(SELECT DISTINCT product_id FROM Product 
 LEFT JOIN Sales USING(product_id) 
 WHERE sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31' 
 OR buyer_id IS NULL)
GROUP BY product_id  