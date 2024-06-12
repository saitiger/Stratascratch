import pandas as pd
import numpy as np

load_df = facebook_web_log[facebook_web_log['action'] == 'page_load'][['user_id', 'timestamp']]
exit_df = facebook_web_log[facebook_web_log['action'] == 'page_exit'][['user_id', 'timestamp']]

df = pd.merge(load_df, exit_df, on='user_id', suffixes=['_load', '_exit'])

df = df[df['timestamp_load'] < df['timestamp_exit']]

df

df['date'] = df['timestamp_load'].dt.floor('d')

df = df.groupby(['user_id', 'date']).agg(timestamp_load=('timestamp_load', 'max'),timestamp_exit=('timestamp_exit', 'min')).reset_index()

df['duration'] = (df['timestamp_exit'] - df['timestamp_load']).dt.total_seconds()  

df.groupby('user_id')['duration'].mean().reset_index()
