import pandas as pd 

friends1 = friendships.rename(columns={'user_name1': 'user', 'user_name2': 'friend'})
friends2 = friendships.rename(columns={'user_name1': 'friend', 'user_name2': 'user'})

friends = pd.concat([friends1, friends2])

merged = user_posts.merge(likes, on='post_id').merge(friends, left_on='user_name', right_on='friend')

merged['day_of_week'] = merged['date_liked'].dt.dayofweek

friday_likes = merged[merged['day_of_week'] == 4]

result = friday_likes.groupby('date_liked')['post_id'].count().reset_index()
result.rename(columns={'post_id': 'likes'}, inplace=True)
