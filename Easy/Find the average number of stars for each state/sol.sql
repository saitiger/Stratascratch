# Solution 1 
select 
state,
avg(stars) num_of_stars
from yelp_business
group by 1 
order by 2 ;

# Solution 2 
select 
state,
sum(stars)/count(*) num_of_stars
from yelp_business
group by 1 
order by 2 ;
