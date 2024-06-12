with cte as (
select 
extract(month from created_at) as mth ,
extract(year from created_at) as yr,
sum(value) as curr_revenue,
lag(sum(value),1) over (order by extract(month from created_at),extract(year from created_at)) as prev_revenue
from 
sf_transactions
group by 1,2
order by 1,2
)
select concat(yr,'-',mth) as year_month,
100.0 * (curr_revenue - prev_revenue)/prev_revenue as revenue_diff_pct
from cte
