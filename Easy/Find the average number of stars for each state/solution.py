import pandas as pd

yelp_business.groupby('state')['stars'].mean().reset_index().rename(columns = {'stars':'num_of_stars'}).sort_values(by = 'num_of_stars')
