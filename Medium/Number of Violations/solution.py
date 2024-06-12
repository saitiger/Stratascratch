import pandas as pd

sf_restaurant_health_violations[sf_restaurant_health_violations['business_name']=='Roxanne Cafe']
.groupby(sf_restaurant_health_violations['inspection_date'].dt.year)
['violation_id'].count().reset_index().sort_values('violation_id',ascending=False)
