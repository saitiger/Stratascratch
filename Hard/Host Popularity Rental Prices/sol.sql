WITH cte AS(
SELECT DISTINCT CONCAT(price, room_type, host_since, zipcode, number_of_reviews) AS id, price,
CASE
WHEN number_of_reviews = 0 THEN 'New'
WHEN number_of_reviews >=1  AND number_of_reviews <=5  THEN 'Rising'
WHEN number_of_reviews >=6  AND number_of_reviews <=15 THEN 'Trending Up'
WHEN number_of_reviews >=16 AND number_of_reviews <=40 THEN 'Popular'
WHEN number_of_reviews >40 THEN 'Hot'
END AS popularity_rating
FROM airbnb_host_searches
)
SELECT popularity_rating,
MIN(price) price_min,
AVG(price) price_avg,
MAX(price) price_max
FROM cte
GROUP BY popularity_rating
