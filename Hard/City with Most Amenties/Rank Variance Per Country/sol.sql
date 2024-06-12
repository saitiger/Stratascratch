with comment_count 
as(select fau.user_id,fcc.number_of_comments, extract(month from created_at) as mth, 
   extract(year from created_at) as yr,
   fau.country from fb_comments_count as fcc inner join fb_active_users fau
on fcc.user_id=fau.user_id),

comment_cntry as(select 
        mth,yr,country,sum(number_of_comments) 
        as tot_cmnt from comment_count
group by 1,2,3),

rnk_cnt as(select mnth,yr,country,
        dense_rank() over(partition by mnth,yr order by tot_cmnt desc) rnk 
        from comment_cntry 
        where mnth in (12,1) and yr in(2019,2020)),

rnk_2019 as(select * from rnk_cnt where mnth=12 and yr=2019),
rnk_2020 as(select * from rnk_cnt where mnth=1 and yr=2020),

cte as(select rnk_2019.country,rnk_2020.rnk as rnk_jan, coalesce(rnk_2019.rnk,1000) as rnk_dec from rnk_2020 left join rnk_2019 on rnk_2020.country=rnk_2019.country)

select country from cte where rnk_dec>rnk_jan;
