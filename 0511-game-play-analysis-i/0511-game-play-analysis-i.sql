# Write your MySQL query statement below
SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id
#SELECT player_id, event_date AS first_login FROM Activity 
#WHERE event_date = (SELECT played_id, MIN(event_date) FROM Activity GROUP BY player_id)