import pandas as pd

num_2020 = car_launches[car_launches['year']==2020].groupby('company_name')['product_name'].count().reset_index()
num_2019 = car_launches[car_launches['year']==2019].groupby('company_name')['product_name'].count().reset_index()

# num_2020 - num_2019
num_2019['net_new_products'] = num_2020['product_name'] - num_2019['product_name']

num_2019 = num_2019[['company_name','net_new_products']]
