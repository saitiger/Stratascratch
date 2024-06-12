with cte as (select
state,
percentile_cont(0.05) within group
(order by fraud_score desc
) percentile
from 
fraud_score
group by 1
)
SELECT fs.policy_num,fs.state,fs.claim_cost,fs.fraud_score
FROM fraud_score fs
JOIN cte c 
ON fs.state = c.state
WHERE fraud_score >= percentile
