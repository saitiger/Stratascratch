-- # Solution 1 

-- Marketing Campaign starts one day later

-- Do not count users who buy the same products from their first day 
-- Clarify if this means all products from Day one or the first product 
-- Seems like it is all products on day one which needs to be excluded 

-- Step 1 Find the first purchase date
WITH first_purchase_date AS (
    SELECT 
        user_id, -- Distinct Users 
        MIN(created_at) as first_purchase_date,
        COUNT(DISTINCT created_at) as num_days_purchased, -- Number of days the user purchased products
        COUNT(DISTINCT product_id) as num_products_purchased -- Number of distinct products the user bought 
    FROM marketing_campaign
    GROUP BY user_id
),
first_day_products AS (
    SELECT 
        fd.user_id,
        STRING_AGG(mc.product_id::text, ',') as first_day_products
    FROM marketing_campaign mc 
    JOIN first_purchase_date fd 
        ON mc.created_at = fd.first_purchase_date
    GROUP BY fd.user_id
),
subsequent_purchases AS (
    SELECT 
        mc.user_id,
        STRING_AGG(DISTINCT mc.product_id::text, ',') as subsequent_products
    FROM marketing_campaign mc
    JOIN first_purchase_date fd 
        ON mc.user_id = fd.user_id 
        AND mc.created_at > fd.first_purchase_date
    GROUP BY mc.user_id
)
SELECT 
    COUNT(DISTINCT fdp.user_id) as users_with_additional_purchases
FROM first_day_products fdp
JOIN first_purchase_date fd ON fdp.user_id = fd.user_id
JOIN subsequent_purchases sp ON fdp.user_id = sp.user_id
WHERE fd.num_days_purchased > 1  -- Users who made purchases on multiple days
  AND sp.subsequent_products IS NOT NULL  -- Users who made subsequent purchases
  AND sp.subsequent_products != fdp.first_day_products  -- Exclude users who bought exactly the same products

-- # Solution 2 
WITH first_purchase AS (
    SELECT user_id,
           MIN(created_at) AS first_order
    FROM marketing_campaign
    GROUP BY user_id
),
valid_users AS (
    SELECT user_id
    FROM marketing_campaign
    GROUP BY user_id
    HAVING COUNT(DISTINCT created_at) > 1
       AND COUNT(DISTINCT product_id) > 1
),
first_products AS (
    SELECT mc.user_id,
           mc.product_id
    FROM marketing_campaign mc
    INNER JOIN first_purchase fp ON mc.user_id = fp.user_id
        AND mc.created_at = fp.first_order
)
SELECT COUNT(DISTINCT mc.user_id) AS user_count
FROM marketing_campaign mc
JOIN valid_users vu ON mc.user_id = vu.user_id
JOIN first_purchase fp ON mc.user_id = fp.user_id
LEFT JOIN first_products fprod ON mc.user_id = fprod.user_id
    AND mc.product_id = fprod.product_id
WHERE fprod.product_id IS NULL  -- Purchases not made on the first day
  AND mc.created_at > fp.first_order;  -- Ensure it's after first day
