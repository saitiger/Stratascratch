WITH active_users AS (
    SELECT country, COUNT(user_id) AS active_user_count
    FROM penetration_analysis
    WHERE ('2024-01-31' - last_active_date)<=30 AND sessions >=5 AND listening_hours >= 10
    GROUP BY 1
),
total_users AS (
    SELECT country,COUNT(user_id) AS total_user_count
    FROM penetration_analysis
    GROUP BY 1
)
SELECT 
    t.country,
    ROUND(a.active_user_count/ t.total_user_count * 100.0, 2) AS active_user_penetration_rate
FROM 
    total_users t
LEFT JOIN 
    active_users a
ON 
    t.country = a.country;
