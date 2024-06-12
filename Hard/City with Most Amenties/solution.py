import pandas as pd

airbnb_search_details['amenties_count_rnk'] = airbnb_search_details['amenities'].apply(lambda x: len(x.split(','))).rank(method='dense',ascending=False)

airbnb_search_details[airbnb_search_details['amenties_count_rnk']==1]['city']
