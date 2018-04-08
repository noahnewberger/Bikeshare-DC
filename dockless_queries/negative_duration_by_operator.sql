select distinct operatorclean,
count(*) as trips,
AVG(EXTRACT(EPOCH FROM endutc - startutc))/60 as avg_duration
from dockless_trips
where EXTRACT(EPOCH FROM endutc - startutc) < 0
group by 1;
