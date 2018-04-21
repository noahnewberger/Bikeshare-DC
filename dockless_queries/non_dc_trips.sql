select distinct 
operatorclean, 
count(*) as total_rides,
sum(case when n_start.nbh_names is null then 1 else 0 end) as start_outside_dc,
sum(case when n_end.nbh_names is null then 1 else 0 end) as end_outside_dc,
sum(case when (n_end.nbh_names is null) or (n_start.nbh_names is null) then 1 else 0 end) as start_or_end_outside_dc,
sum(case when (n_end.nbh_names is null) and (n_start.nbh_names is null) then 1 else 0 end) as start_and_end_outside_dc,
sum(case when (n_end.nbh_names is null) or (n_start.nbh_names is null) then 1 else 0 end)/count(*)::float as pct_start_or_end
from dockless_trips as d
left join dockless_ngh_lookup n_start
on d.startlongitude = n_start.lon and d.startlatitude = n_start.lat
left join dockless_ngh_lookup n_end
on d.endlongitude = n_end.lon and d.endlatitude = n_end.lat
group by 1;