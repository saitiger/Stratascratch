select trackname,count(*) as times_top1 from spotify_worldwide_daily_song_ranking
where position = 1
group by trackname
order by 2 desc
