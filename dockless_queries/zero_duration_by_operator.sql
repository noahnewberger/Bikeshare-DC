select distinct operatorclean,
count(*) as total_trips,
sum(CASE WHEN EXTRACT(EPOCH FROM endutc - startutc) = 0 then 1
     ELSE 0 END) as total_zero_trips,
sum(CASE WHEN EXTRACT(EPOCH FROM endutc - startutc) = 0 then 1
     ELSE 0 END)/count(*)::float * 100 as perc_zero_dur
from dockless_trips
group by 1;