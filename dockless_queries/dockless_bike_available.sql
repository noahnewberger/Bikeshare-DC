select distinct
operatorclean,
count(*) as total_bikes_used,
avg(bike_age) as bike_age
from 
(select distinct 
operatorclean, 
bikeid,
min(startutc::date) as first_ride,
(date_trunc('day', max(startutc)) + interval '1 day')::date as last_ride_plus,
(date_trunc('day', max(startutc)) + interval '1 day')::date - min(startutc::date) as bike_age
from dockless_trips
group by 1, 2) as bike_age
group by 1;