# Write your MySQL query statement below
SELECT t.id FROM Weather t JOIN Weather y ON 
subdate(t.recordDate, 1) = y.recordDate AND t.temperature > y.temperature