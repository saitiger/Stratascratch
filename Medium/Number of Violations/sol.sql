SELECT EXTRACT (YEAR
                FROM inspection_date :: DATE) AS YEAR,
               count(*) AS n_inspections
FROM sf_restaurant_health_violations
WHERE business_name = 'Roxanne Cafe'
  AND violation_id IS NOT NULL
GROUP BY YEAR
ORDER BY YEAR ASC
