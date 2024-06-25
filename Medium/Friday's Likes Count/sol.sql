with friends as (
select user_name1 user , user_name2 friend
from friendships
union  
select user_name2,user_name1
from friendships
)
select l.date_liked,count(l.post_id) likes
from user_posts up
join 
likes l
on up.post_id = l.post_id
join friends f
on f.friend = l.user_name
where EXTRACT(DOW FROM date_liked) = 5
group by 1
