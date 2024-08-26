select 
year,
sum(money_spent) total_cost,
sum(customers_acquired) total_number_of_customers_acquired
from uber_advertising
group by 1 ;
