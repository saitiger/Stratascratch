yelp_reviews.groupby('stars')['review_id'].count().reset_index().rename(columns = {'review_id':'num_stars'}).sort_values(by = 'stars')
