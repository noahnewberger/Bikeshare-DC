select distinct
v2.tripid,
org.userid
from dockless_trips_v2 as v2
left join dockless_trips as org
on v2.startutc=org.startutc 
and v2.endutc=org.endutc
and v2.operatorclean=org.operatorclean
and v2.startlatitude=org.startlatitude
and v2.startlongitude=org.startlongitude
and v2.endlatitude=org.endlatitude
and v2.endlongitude=org.endlongitude
where v2.operatorclean='lime' and v2.userid='0' and org.userid is null;