with cte1 as (
select user_id,
extract(day from timestamp) as dt,
min(timestamp) as earliest_exit 
from
facebook_web_log
where action = 'page_exit'
group by user_id,
extract(day from timestamp)
),
cte2 as(
select user_id,
extract(day from timestamp) as dt,
max(timestamp) as latest_load
from
facebook_web_log
where action = 'page_load'
group by user_id,
extract(day from timestamp)
)
select c1.user_id,
avg(earliest_exit - latest_load) as diff
from cte1 c1 join cte2 c2
on c1.user_id = c2.user_id 
group by 1
