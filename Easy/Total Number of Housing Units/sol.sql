SELECT year,
       SUM(south + west + midwest + northeast)  AS n_units
FROM housing_units_completed_us
GROUP BY 1
ORDER BY 1
