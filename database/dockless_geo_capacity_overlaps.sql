SELECT closest_station.*,
CASE WHEN closest_station.dist_miles <= 0.25 then 1 else 0 end as geo_start_overlap,
CASE WHEN out_hist.status = 'empty' and closest_station.dist_miles <= 0.25 then 1 else 0 end as capacity_overlap 
FROM
/* Find the closest CaBi station and calculate the distance in miles*/
(SELECT dan.location_id,
dan.created, 
station.short_name,
ST_Distance(dan.location, ST_SetSRID(st_makepoint(station.lon, station.lat),4326)) * 0.000621371 as dist_miles
FROM dan_dockless as dan
CROSS JOIN LATERAL
(SELECT short_name, lon, lat
   FROM cabi_stations_temp
   ORDER BY
     dan.location <-> ST_SetSRID(st_makepoint(lon, lat),4326)
   LIMIT 1) as station) as closest_station
/* IMPORTANT: For the real dockless data we'll need to determine if the end point is also a geo overlap*/
/* For the closest CaBi station, look up if there is an CaBi outage at said station when the ride started*/
LEFT JOIN cabi_out_hist as out_hist
ON (closest_station.short_name = out_hist.terminal_number) AND (closest_station.created BETWEEN out_hist.start_time AND out_hist.end_time)
;