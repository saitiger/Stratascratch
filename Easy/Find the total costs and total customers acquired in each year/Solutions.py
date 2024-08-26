import pandas as pd

result = uber_advertising.groupby('year').agg(
    total_cost=pd.NamedAgg(column='money_spent', aggfunc='sum'),
    total_number_of_customers_acquired=pd.NamedAgg(column='customers_acquired', aggfunc='sum')
).reset_index()

result
