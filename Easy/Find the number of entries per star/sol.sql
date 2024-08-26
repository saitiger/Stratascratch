select stars,
count(*) num_of_entries
from 
yelp_reviews
group by 1
order by 1 ;
