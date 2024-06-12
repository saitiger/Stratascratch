with email_count as (
select 
from_user,
count(from_user) total_emails
from google_gmail_emails
group by 1
)
select from_user,
total_emails,
rank() over(order by total_emails desc,from_user) "row_number"
from
email_count
order by 3
