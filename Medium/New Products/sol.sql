select company_name,
sum(case when year = 2020 then 1 else - 1 end) net_products
from car_launches
group by 
company_name;
