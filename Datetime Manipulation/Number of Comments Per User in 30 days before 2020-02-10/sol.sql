-- Get total comments received by each user in the 30 days before 2020-02-10
-- Using date arithmetic to calculate the range dynamically

SELECT 
    u.user_id,
    u.username,
    COUNT(c.comment_id) as total_comments_received
FROM 
    users u
    INNER JOIN comments c ON u.user_id = c.target_user_id
WHERE 
    c.created_date >= '2020-02-10'::date - INTERVAL '30 days'
    AND c.created_date < '2020-02-10'::date
GROUP BY 
    u.user_id, u.username
ORDER BY 
    total_comments_received DESC, u.username;
