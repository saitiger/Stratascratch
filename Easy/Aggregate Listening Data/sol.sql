select
user_id,
round(sum(listen_duration)/60.0) total_listen_duration,
count(distinct song_id) unique_song_count
from listening_habits
group by 1;
