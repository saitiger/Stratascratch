WITH valid_users AS
(
SELECT 
user_id,
100.0*SUM(CASE WHEN event_type IN ('video call received','video call sent','voice call received','voice call sent') THEN 1 ELSE 0 END)/COUNT(*) pct_valid_event
FROM 
fact_events
GROUP BY user_id
HAVING 
100.0*SUM(CASE WHEN event_type IN ('video call received','video call sent','voice call received','voice call sent') THEN 1 ELSE 0 END)/COUNT(*)>=50
),
client_count AS 
(
SELECT client_id,COUNT(*) cnt 
FROM 
fact_events 
WHERE 
user_id in (SELECT user_id FROM valid_users GROUP BY user_id)
GROUP BY client_id
)
SELECT client_id
FROM 
client_count
ORDER BY 
cnt DESC 
LIMIT 1 
