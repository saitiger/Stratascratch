import pandas as pd

res = (listening_habits
       .groupby('user_id')
       .agg({'song_id': 'nunique', 'listen_duration': 'sum'})
       .reset_index()
       .rename(columns={'song_id': 'unique_song_count', 'listen_duration': 'total_listen_duration'})
)

res['total_listen_duration'] = (res['total_listen_duration'] / 60.0).round().astype(int)

res
