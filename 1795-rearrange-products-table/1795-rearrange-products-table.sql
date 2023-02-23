# Write your MySQL query statement below
SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE NOT store1 IS NULL
UNION ALL 
SELECT product_id, 'store2', store2 AS price FROM Products WHERE NOT store2 IS NULL
UNION ALL
SELECT product_id, 'store3', store3 AS price FROM Products WHERE NOT store3 IS NULL
