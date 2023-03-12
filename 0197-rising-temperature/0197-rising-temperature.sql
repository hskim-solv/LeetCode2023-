# Write your MySQL query statement below
SELECT t.id FROM Weather t JOIN Weather y ON (TIMESTAMPDIFF(DAY, y.recordDate, t.recordDate)=1 AND t.temperature-y.temperature > 0)
#SELECT t.id,t.temperature,y.recordDate, y.temperature FROM Weather t LEFT JOIN Weather y ON (t.recordDate-y.recordDate = 1) WHERE t.id =407