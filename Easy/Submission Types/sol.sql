# Solution 1 
SELECT user_id
FROM submissions
WHERE submission_type IN ('Refinance', 'InSchool')
GROUP BY user_id
HAVING COUNT(DISTINCT CASE WHEN submission_type = 'Refinance' THEN submission_type END) > 0
   AND COUNT(DISTINCT CASE WHEN submission_type = 'InSchool' THEN submission_type END) > 0;

# Solution 2 
select user_id from(
select user_id,
sum(case when type = 'Refinance' then 1 else 0 end) cnt_refinance,
sum(case when type = 'InSchool' then 1 else 0 end) cnt_inschool
from loans
group by 1)x
where cnt_refinance>=1 and cnt_inschool>=1
