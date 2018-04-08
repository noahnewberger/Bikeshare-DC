select distinct operatorclean,
EXTRACT(EPOCH FROM enddate - startdate)::int/60 as time_diff, 
count(*) as trips
from dockless_trips group by 1, 2
order by 1,2;