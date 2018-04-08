select distinct operatorclean,
count(*) as trips,
avg(EXTRACT(EPOCH FROM enddate - startdate)::int/60) as avg_duration 
from dockless_trips
where EXTRACT(EPOCH FROM enddate - startdate)::int/60 > 0
group by 1;