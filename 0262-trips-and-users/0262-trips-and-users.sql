
#SELECT request_at AS Day, ROUND(IFNULL(son, 0) / pa, 2) AS 'Cancellation Rate' FROM (SELECT request_at, COUNT(status) AS son FROM Trips JOIN (SELECT users_id AS client_id FROM Users WHERE role='client' AND banned = 'No') uc USING(client_id) WHERE status LIKE "cancelled%" GROUP BY request_at) r1 RIGHT JOIN (SELECT request_at, COUNT(status) AS pa FROM Trips JOIN (SELECT users_id AS client_id FROM Users WHERE role='client' AND banned = 'No') uc USING(client_id) GROUP BY request_at) r2 USING(request_at)



select t.Request_at Day,
       ROUND((count(IF(t.status!='completed',TRUE,null))/count(*)),2) as 'Cancellation Rate'
from Trips t where 
t.Client_Id in (Select Users_Id from Users where Banned='No') 
and t.Driver_Id in (Select Users_Id from Users where Banned='No')
and t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at;