with count_friends as (
select user1,count(*) num_friends
from(
select user1,user2 
from 
facebook_friends
union all
select user2,user1 
from facebook_friends
)A
group by 1 
)
select user1,
sum(num_friends)/(select count(distinct user1) from count_friends)*100
popularity_percentage
from count_friends
group by 1 
order by 1 
