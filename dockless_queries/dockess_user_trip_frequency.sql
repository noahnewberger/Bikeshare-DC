select distinct 
user_freqs.operatorclean,
user_freqs.user_trips,
count(*) as freq_user_trips,
from
((select distinct
operatorclean,
userid,
count(*) as user_trips
from dockless_trips
where operatorclean in ('mobike', 'lime', 'spin')
group by 1, 2
order by operatorclean, count(*))
union
/*ofo users*/
(select distinct
'ofo' as operatorclean,
userid,
sum(trips) as user_trips
from ofo_users
group by 1, 2
order by operatorclean, sum(trips))
union
/*ofo users*/
(select distinct
'jump' as operatorclean,
userid,
sum(trips) as user_trips
from jump_users
group by 1, 2
order by operatorclean, sum(trips))) as user_freqs
group by 1, 2
order by 1, 2;