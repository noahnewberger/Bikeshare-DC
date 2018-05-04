# Data Dictionary

## Georgetown Capstone Team Bikeshare

  
  

**acs**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
acs_id | bigint | NO | None
year | integer | YES | None
datanum | integer | YES | None
serial | integer | YES | None
hhwt | integer | YES | None
stateicp | integer | YES | None
statefip | integer | YES | None
county | integer | YES | None
countyfips | integer | YES | None
metarea | numeric | YES | None
metaread | numeric | YES | None
city | integer | YES | None
citypop | integer | YES | None
gq | integer | YES | None
pernum | integer | YES | None
perwt | integer | YES | None
sex | integer | YES | None
age | integer | YES | None
race | integer | YES | None
raced | integer | YES | None
citizen | integer | YES | None
racesing | numeric | YES | None
racesingd | numeric | YES | None
racamind | integer | YES | None
racasian | integer | YES | None
racblk | integer | YES | None
racpacis | integer | YES | None
racwht | integer | YES | None
racother | integer | YES | None
empstat | integer | YES | None
empstatd | integer | YES | None
labforce | integer | YES | None
wkswork1 | numeric | YES | None
inctot | integer | YES | None
ftotinc | integer | YES | None
incwage | integer | YES | None
pwstate2 | integer | YES | None
tranwork | integer | YES | None
carpool | integer | YES | None
riders | integer | YES | None
trantime | integer | YES | None
qtrantim | integer | YES | None
qtranwor | integer | YES | None

**anc**: DC Advisory Neighborhood Commissions converted from Open Data DC GeoJSON

Attribute | Type | Nullable | Description
--- | --- | --- | ---
anc_id | character varying | YES | ANC name with Ward Number and ANC Letter (ie "6B")
name | character varying | YES | Same as anc_id with "ANC " concatenated prior (ie "ANC 6B")
objectid | integer | NO | None
shape_area | numeric | YES | None
shape_length | numeric | YES | None
web_url | character varying | YES | None
polygon | USER-DEFINED | YES | None

**bike_events**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
id | character varying | NO | None
final_date | date | YES | None
summary | character varying | YES | None

**cabi_membership**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
month | date | NO | None
annual_member_purch | numeric | YES | None
monthly_member_purch | numeric | YES | None
day_key_member_purch | numeric | YES | None
multi_day_pass_purch | numeric | YES | None
single_day_pass_purch | numeric | YES | None
single_trip_pass_purch | numeric | YES | None

**cabi_out_hist**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
terminal_number | character varying | YES | None
status | character varying | YES | None
start_time | timestamp without time zone | YES | None
end_time | timestamp without time zone | YES | None
duration | integer | YES | None
outage_id | integer | NO | None

**cabi_price**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
min_seconds | integer | NO | None
max_seconds | integer | YES | None
casual_cost | numeric | YES | None
member_cost | numeric | YES | None

**cabi_stations_geo_temp**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
start_short_name | character varying | YES | None
end_short_name | character varying | YES | None
start_capacity | integer | YES | None
start_eightd_has_key_dispenser | boolean | YES | None
start_lat | numeric | YES | None
start_lon | numeric | YES | None
start_name | character varying | YES | None
start_region_id | integer | YES | None
start_rental_methods | character varying | YES | None
start_rental_url | character varying | YES | None
start_station_id | integer | YES | None
start_region_code | character varying | YES | None
start_cluster_name | character varying | YES | None
start_ngh_names | character varying | YES | None
start_anc | character varying | YES | None
start_ward | character varying | YES | None
end_capacity | integer | YES | None
end_eightd_has_key_dispenser | boolean | YES | None
end_lat | numeric | YES | None
end_lon | numeric | YES | None
end_name | character varying | YES | None
end_region_id | integer | YES | None
end_rental_methods | character varying | YES | None
end_rental_url | character varying | YES | None
end_station_id | integer | YES | None
end_region_code | character varying | YES | None
end_cluster_name | character varying | YES | None
end_ngh_names | character varying | YES | None
end_anc | character varying | YES | None
end_ward | character varying | YES | None
dist_miles | numeric | YES | None

**cabi_stations_temp**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
capacity | integer | YES | None
eightd_has_key_dispenser | boolean | YES | None
eightd_station_services | character varying | YES | None
lat | numeric | YES | None
lon | numeric | YES | None
name | character varying | YES | None
region_id | integer | YES | None
rental_methods | character varying | YES | None
rental_url | character varying | YES | None
short_name | character varying | YES | None
station_id | integer | NO | None

**cabi_system**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
region_id | integer | NO | None
name | character varying | YES | None
code | text | YES | None

**cabi_trips**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
duration | integer | YES | None
start_date | timestamp without time zone | YES | None
end_date | timestamp without time zone | YES | None
start_station | character varying | YES | None
end_station | character varying | YES | None
bike_number | character varying | YES | None
member_type | character varying | YES | None
trip_id | bigint | NO | None

**cabi_trips_membertype**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
startdate | timestamp without time zone | YES | None
enddate | timestamp without time zone | YES | None
bikenumber | character varying | YES | None
member_type | character varying | YES | None
trip_id | character varying | NO | None

**dan_dockless**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
location_id | character varying | YES | None
location | USER-DEFINED | YES | None
provider | character varying | YES | None
bike_id | character varying | YES | None
created | timestamp without time zone | YES | None

**dark_sky_raw**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
apparenttemperaturehigh | numeric | YES | None
apparenttemperaturehightime | integer | YES | None
apparenttemperaturelow | numeric | YES | None
apparenttemperaturelowtime | integer | YES | None
apparenttemperaturemax | numeric | YES | None
apparenttemperaturemaxtime | integer | YES | None
apparenttemperaturemin | numeric | YES | None
apparenttemperaturemintime | integer | YES | None
cloudcover | numeric | YES | None
dewpoint | numeric | YES | None
humidity | numeric | YES | None
icon | character varying | YES | None
moonphase | numeric | YES | None
precipaccumulation | numeric | YES | None
precipintensity | numeric | YES | None
precipintensitymax | numeric | YES | None
precipintensitymaxtime | integer | YES | None
precipprobability | numeric | YES | None
preciptype | character varying | YES | None
pressure | numeric | YES | None
summary | character varying | YES | None
sunrisetime | integer | YES | None
sunsettime | integer | YES | None
temperaturehigh | numeric | YES | None
temperaturehightime | integer | YES | None
temperaturelow | numeric | YES | None
temperaturelowtime | integer | YES | None
temperaturemax | numeric | YES | None
temperaturemaxtime | integer | YES | None
temperaturemin | numeric | YES | None
temperaturemintime | integer | YES | None
day_time | integer | YES | None
visibility | numeric | YES | None
weather_date | date | NO | None
windbearing | numeric | YES | None
windspeed | numeric | YES | None

**dc_pop**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
pop_date | timestamp without time zone | NO | None
citypop | numeric | YES | None
grow_rate | numeric | YES | None
pct_bike | numeric | YES | None

**dockless_bikes_api**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
date | date | YES | None
operator | text | YES | None
bikes_available | integer | YES | None

**dockless_price**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
min_seconds | integer | NO | None
max_seconds | integer | YES | None
limebike | numeric | YES | None
spin | numeric | YES | None
ofo | numeric | YES | None
mobike | numeric | YES | None

**dockless_summary**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
operator | text | YES | None
month | date | YES | None
totaltrips | numeric | YES | None
totalbikes | numeric | YES | None

**dockless_trips**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
x | integer | YES | None
operator | character varying | YES | None
tripid | character varying | NO | None
bikeid | character varying | YES | None
userid | character varying | YES | None
startdate | timestamp without time zone | YES | None
enddate | timestamp without time zone | YES | None
startlatitude | numeric | YES | None
startlongitude | numeric | YES | None
endlatitude | numeric | YES | None
endlongitude | numeric | YES | None
tripdistance | numeric | YES | None
metersmoved | numeric | YES | None
startward | numeric | YES | None
endward | numeric | YES | None
distance | numeric | YES | None
posct | timestamp without time zone | YES | None
endposct | timestamp without time zone | YES | None
startutc | timestamp without time zone | YES | None
endutc | timestamp without time zone | YES | None
uniquetripid | character varying | YES | None
operatorclean | character varying | YES | None

**dockless_trips_geo**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
tripid | character varying | YES | None
uniquetripid | character varying | YES | None
operatorclean | character varying | YES | None
bikeid | character varying | YES | None
userid | character varying | YES | None
startutc | timestamp without time zone | YES | None
endutc | timestamp without time zone | YES | None
start_anc | character varying | YES | None
end_anc | character varying | YES | None
startlatitude | numeric | YES | None
startlongitude | numeric | YES | None
endlatitude | numeric | YES | None
endlongitude | numeric | YES | None
tripdistance_meters_calc | double precision | YES | None
stcabi_distance_meters | double precision | YES | None
st_station | character varying | YES | None
st_station_status | character varying | YES | None
st_geo_overlap | integer | YES | None
st_cap_overlap | integer | YES | None
endcabi_distance_meters | double precision | YES | None
end_station | character varying | YES | None
end_geo_overlap | integer | YES | None

**final_db**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
date | date | NO | None
year | numeric | YES | None
quarter | numeric | YES | None
month | numeric | YES | None
day_of_week | numeric | YES | None
apparenttemperaturehightime | numeric | YES | None
apparenttemperaturelowtime | numeric | YES | None
temperaturehightime | numeric | YES | None
temperaturelowtime | numeric | YES | None
precipintensitymaxtime | numeric | YES | None
sunrisetime | numeric | YES | None
sunsettime | numeric | YES | None
day_time | numeric | YES | None
daylight_hours | numeric | YES | None
apparenttemperaturehigh | numeric | YES | None
apparenttemperaturelow | numeric | YES | None
temperaturehigh | numeric | YES | None
temperaturelow | numeric | YES | None
cloudcover | numeric | YES | None
dewpoint | numeric | YES | None
humidity | numeric | YES | None
moonphase | numeric | YES | None
precipaccumulation | numeric | YES | None
precipintensity | numeric | YES | None
precipintensitymax | numeric | YES | None
precipprobability | numeric | YES | None
pressure | numeric | YES | None
rain | numeric | YES | None
snow | numeric | YES | None
sleet | numeric | YES | None
visibility | numeric | YES | None
windbearing | numeric | YES | None
windspeed | numeric | YES | None
nats_games | numeric | YES | None
nats_attendance | numeric | YES | None
dc_bike_event | numeric | YES | None
dc_pop | numeric | YES | None
cabi_trips | numeric | YES | None
cabi_trip_dur_tot | numeric | YES | None
cabi_trip_dist_tot | numeric | YES | None
cabi_trip_cost_tot | numeric | YES | None
cabi_trip_dur_avg | numeric | YES | None
cabi_trip_dist_avg | numeric | YES | None
cabi_trip_cost_avg | numeric | YES | None
cabi_trips_casual | numeric | YES | None
cabi_trips_member | numeric | YES | None
cabi_trips_unknown | numeric | YES | None
cabi_trip_dur_tot_casual | numeric | YES | None
cabi_trip_dur_tot_member | numeric | YES | None
cabi_trip_dur_tot_unknown | numeric | YES | None
cabi_trip_dist_tot_casual | numeric | YES | None
cabi_trip_dist_tot_member | numeric | YES | None
cabi_trip_dist_tot_unknown | numeric | YES | None
cabi_trip_cost_tot_casual | numeric | YES | None
cabi_trip_cost_tot_member | numeric | YES | None
cabi_trip_cost_tot_unknown | numeric | YES | None
cabi_trip_dur_avg_casual | numeric | YES | None
cabi_trip_dur_avg_member | numeric | YES | None
cabi_trip_dur_avg_unknown | numeric | YES | None
cabi_trip_dist_avg_casual | numeric | YES | None
cabi_trip_dist_avg_member | numeric | YES | None
cabi_trip_dist_avg_unknown | numeric | YES | None
cabi_trip_cost_avg_casual | numeric | YES | None
cabi_trip_cost_avg_member | numeric | YES | None
cabi_trip_cost_avg_unknown | numeric | YES | None
cabi_trips_alx_to_alx | numeric | YES | None
cabi_trips_alx_to_arl | numeric | YES | None
cabi_trips_alx_to_ffx | numeric | YES | None
cabi_trips_alx_to_mcn | numeric | YES | None
cabi_trips_alx_to_mcs | numeric | YES | None
cabi_trips_alx_to_wdc | numeric | YES | None
cabi_trips_arl_to_alx | numeric | YES | None
cabi_trips_arl_to_arl | numeric | YES | None
cabi_trips_arl_to_ffx | numeric | YES | None
cabi_trips_arl_to_mcn | numeric | YES | None
cabi_trips_arl_to_mcs | numeric | YES | None
cabi_trips_arl_to_wdc | numeric | YES | None
cabi_trips_ffx_to_alx | numeric | YES | None
cabi_trips_ffx_to_arl | numeric | YES | None
cabi_trips_ffx_to_ffx | numeric | YES | None
cabi_trips_ffx_to_mcs | numeric | YES | None
cabi_trips_ffx_to_wdc | numeric | YES | None
cabi_trips_mcn_to_arl | numeric | YES | None
cabi_trips_mcn_to_mcn | numeric | YES | None
cabi_trips_mcn_to_mcs | numeric | YES | None
cabi_trips_mcn_to_wdc | numeric | YES | None
cabi_trips_mcs_to_alx | numeric | YES | None
cabi_trips_mcs_to_arl | numeric | YES | None
cabi_trips_mcs_to_ffx | numeric | YES | None
cabi_trips_mcs_to_mcn | numeric | YES | None
cabi_trips_mcs_to_mcs | numeric | YES | None
cabi_trips_mcs_to_wdc | numeric | YES | None
cabi_trips_wdc_to_alx | numeric | YES | None
cabi_trips_wdc_to_arl | numeric | YES | None
cabi_trips_wdc_to_ffx | numeric | YES | None
cabi_trips_wdc_to_mcn | numeric | YES | None
cabi_trips_wdc_to_mcs | numeric | YES | None
cabi_trips_wdc_to_wdc | numeric | YES | None
cabi_trip_dur_tot_alx_to_alx | numeric | YES | None
cabi_trip_dur_tot_alx_to_arl | numeric | YES | None
cabi_trip_dur_tot_alx_to_ffx | numeric | YES | None
cabi_trip_dur_tot_alx_to_mcn | numeric | YES | None
cabi_trip_dur_tot_alx_to_mcs | numeric | YES | None
cabi_trip_dur_tot_alx_to_wdc | numeric | YES | None
cabi_trip_dur_tot_arl_to_alx | numeric | YES | None
cabi_trip_dur_tot_arl_to_arl | numeric | YES | None
cabi_trip_dur_tot_arl_to_ffx | numeric | YES | None
cabi_trip_dur_tot_arl_to_mcn | numeric | YES | None
cabi_trip_dur_tot_arl_to_mcs | numeric | YES | None
cabi_trip_dur_tot_arl_to_wdc | numeric | YES | None
cabi_trip_dur_tot_ffx_to_alx | numeric | YES | None
cabi_trip_dur_tot_ffx_to_arl | numeric | YES | None
cabi_trip_dur_tot_ffx_to_ffx | numeric | YES | None
cabi_trip_dur_tot_ffx_to_mcs | numeric | YES | None
cabi_trip_dur_tot_ffx_to_wdc | numeric | YES | None
cabi_trip_dur_tot_mcn_to_arl | numeric | YES | None
cabi_trip_dur_tot_mcn_to_mcn | numeric | YES | None
cabi_trip_dur_tot_mcn_to_mcs | numeric | YES | None
cabi_trip_dur_tot_mcn_to_wdc | numeric | YES | None
cabi_trip_dur_tot_mcs_to_alx | numeric | YES | None
cabi_trip_dur_tot_mcs_to_arl | numeric | YES | None
cabi_trip_dur_tot_mcs_to_ffx | numeric | YES | None
cabi_trip_dur_tot_mcs_to_mcn | numeric | YES | None
cabi_trip_dur_tot_mcs_to_mcs | numeric | YES | None
cabi_trip_dur_tot_mcs_to_wdc | numeric | YES | None
cabi_trip_dur_tot_wdc_to_alx | numeric | YES | None
cabi_trip_dur_tot_wdc_to_arl | numeric | YES | None
cabi_trip_dur_tot_wdc_to_ffx | numeric | YES | None
cabi_trip_dur_tot_wdc_to_mcn | numeric | YES | None
cabi_trip_dur_tot_wdc_to_mcs | numeric | YES | None
cabi_trip_dur_tot_wdc_to_wdc | numeric | YES | None
cabi_trip_dist_tot_alx_to_alx | numeric | YES | None
cabi_trip_dist_tot_alx_to_arl | numeric | YES | None
cabi_trip_dist_tot_alx_to_ffx | numeric | YES | None
cabi_trip_dist_tot_alx_to_mcn | numeric | YES | None
cabi_trip_dist_tot_alx_to_mcs | numeric | YES | None
cabi_trip_dist_tot_alx_to_wdc | numeric | YES | None
cabi_trip_dist_tot_arl_to_alx | numeric | YES | None
cabi_trip_dist_tot_arl_to_arl | numeric | YES | None
cabi_trip_dist_tot_arl_to_ffx | numeric | YES | None
cabi_trip_dist_tot_arl_to_mcn | numeric | YES | None
cabi_trip_dist_tot_arl_to_mcs | numeric | YES | None
cabi_trip_dist_tot_arl_to_wdc | numeric | YES | None
cabi_trip_dist_tot_ffx_to_alx | numeric | YES | None
cabi_trip_dist_tot_ffx_to_arl | numeric | YES | None
cabi_trip_dist_tot_ffx_to_ffx | numeric | YES | None
cabi_trip_dist_tot_ffx_to_mcs | numeric | YES | None
cabi_trip_dist_tot_ffx_to_wdc | numeric | YES | None
cabi_trip_dist_tot_mcn_to_arl | numeric | YES | None
cabi_trip_dist_tot_mcn_to_mcn | numeric | YES | None
cabi_trip_dist_tot_mcn_to_mcs | numeric | YES | None
cabi_trip_dist_tot_mcn_to_wdc | numeric | YES | None
cabi_trip_dist_tot_mcs_to_alx | numeric | YES | None
cabi_trip_dist_tot_mcs_to_arl | numeric | YES | None
cabi_trip_dist_tot_mcs_to_ffx | numeric | YES | None
cabi_trip_dist_tot_mcs_to_mcn | numeric | YES | None
cabi_trip_dist_tot_mcs_to_mcs | numeric | YES | None
cabi_trip_dist_tot_mcs_to_wdc | numeric | YES | None
cabi_trip_dist_tot_wdc_to_alx | numeric | YES | None
cabi_trip_dist_tot_wdc_to_arl | numeric | YES | None
cabi_trip_dist_tot_wdc_to_ffx | numeric | YES | None
cabi_trip_dist_tot_wdc_to_mcn | numeric | YES | None
cabi_trip_dist_tot_wdc_to_mcs | numeric | YES | None
cabi_trip_dist_tot_wdc_to_wdc | numeric | YES | None
cabi_trip_cost_tot_alx_to_alx | numeric | YES | None
cabi_trip_cost_tot_alx_to_arl | numeric | YES | None
cabi_trip_cost_tot_alx_to_ffx | numeric | YES | None
cabi_trip_cost_tot_alx_to_mcn | numeric | YES | None
cabi_trip_cost_tot_alx_to_mcs | numeric | YES | None
cabi_trip_cost_tot_alx_to_wdc | numeric | YES | None
cabi_trip_cost_tot_arl_to_alx | numeric | YES | None
cabi_trip_cost_tot_arl_to_arl | numeric | YES | None
cabi_trip_cost_tot_arl_to_ffx | numeric | YES | None
cabi_trip_cost_tot_arl_to_mcn | numeric | YES | None
cabi_trip_cost_tot_arl_to_mcs | numeric | YES | None
cabi_trip_cost_tot_arl_to_wdc | numeric | YES | None
cabi_trip_cost_tot_ffx_to_alx | numeric | YES | None
cabi_trip_cost_tot_ffx_to_arl | numeric | YES | None
cabi_trip_cost_tot_ffx_to_ffx | numeric | YES | None
cabi_trip_cost_tot_ffx_to_mcs | numeric | YES | None
cabi_trip_cost_tot_ffx_to_wdc | numeric | YES | None
cabi_trip_cost_tot_mcn_to_arl | numeric | YES | None
cabi_trip_cost_tot_mcn_to_mcn | numeric | YES | None
cabi_trip_cost_tot_mcn_to_mcs | numeric | YES | None
cabi_trip_cost_tot_mcn_to_wdc | numeric | YES | None
cabi_trip_cost_tot_mcs_to_alx | numeric | YES | None
cabi_trip_cost_tot_mcs_to_arl | numeric | YES | None
cabi_trip_cost_tot_mcs_to_ffx | numeric | YES | None
cabi_trip_cost_tot_mcs_to_mcn | numeric | YES | None
cabi_trip_cost_tot_mcs_to_mcs | numeric | YES | None
cabi_trip_cost_tot_mcs_to_wdc | numeric | YES | None
cabi_trip_cost_tot_wdc_to_alx | numeric | YES | None
cabi_trip_cost_tot_wdc_to_arl | numeric | YES | None
cabi_trip_cost_tot_wdc_to_ffx | numeric | YES | None
cabi_trip_cost_tot_wdc_to_mcn | numeric | YES | None
cabi_trip_cost_tot_wdc_to_mcs | numeric | YES | None
cabi_trip_cost_tot_wdc_to_wdc | numeric | YES | None
cabi_trip_dur_avg_alx_to_alx | numeric | YES | None
cabi_trip_dur_avg_alx_to_arl | numeric | YES | None
cabi_trip_dur_avg_alx_to_ffx | numeric | YES | None
cabi_trip_dur_avg_alx_to_mcn | numeric | YES | None
cabi_trip_dur_avg_alx_to_mcs | numeric | YES | None
cabi_trip_dur_avg_alx_to_wdc | numeric | YES | None
cabi_trip_dur_avg_arl_to_alx | numeric | YES | None
cabi_trip_dur_avg_arl_to_arl | numeric | YES | None
cabi_trip_dur_avg_arl_to_ffx | numeric | YES | None
cabi_trip_dur_avg_arl_to_mcn | numeric | YES | None
cabi_trip_dur_avg_arl_to_mcs | numeric | YES | None
cabi_trip_dur_avg_arl_to_wdc | numeric | YES | None
cabi_trip_dur_avg_ffx_to_alx | numeric | YES | None
cabi_trip_dur_avg_ffx_to_arl | numeric | YES | None
cabi_trip_dur_avg_ffx_to_ffx | numeric | YES | None
cabi_trip_dur_avg_ffx_to_mcs | numeric | YES | None
cabi_trip_dur_avg_ffx_to_wdc | numeric | YES | None
cabi_trip_dur_avg_mcn_to_arl | numeric | YES | None
cabi_trip_dur_avg_mcn_to_mcn | numeric | YES | None
cabi_trip_dur_avg_mcn_to_mcs | numeric | YES | None
cabi_trip_dur_avg_mcn_to_wdc | numeric | YES | None
cabi_trip_dur_avg_mcs_to_alx | numeric | YES | None
cabi_trip_dur_avg_mcs_to_arl | numeric | YES | None
cabi_trip_dur_avg_mcs_to_ffx | numeric | YES | None
cabi_trip_dur_avg_mcs_to_mcn | numeric | YES | None
cabi_trip_dur_avg_mcs_to_mcs | numeric | YES | None
cabi_trip_dur_avg_mcs_to_wdc | numeric | YES | None
cabi_trip_dur_avg_wdc_to_alx | numeric | YES | None
cabi_trip_dur_avg_wdc_to_arl | numeric | YES | None
cabi_trip_dur_avg_wdc_to_ffx | numeric | YES | None
cabi_trip_dur_avg_wdc_to_mcn | numeric | YES | None
cabi_trip_dur_avg_wdc_to_mcs | numeric | YES | None
cabi_trip_dur_avg_wdc_to_wdc | numeric | YES | None
cabi_trip_dist_avg_alx_to_alx | numeric | YES | None
cabi_trip_dist_avg_alx_to_arl | numeric | YES | None
cabi_trip_dist_avg_alx_to_ffx | numeric | YES | None
cabi_trip_dist_avg_alx_to_mcn | numeric | YES | None
cabi_trip_dist_avg_alx_to_mcs | numeric | YES | None
cabi_trip_dist_avg_alx_to_wdc | numeric | YES | None
cabi_trip_dist_avg_arl_to_alx | numeric | YES | None
cabi_trip_dist_avg_arl_to_arl | numeric | YES | None
cabi_trip_dist_avg_arl_to_ffx | numeric | YES | None
cabi_trip_dist_avg_arl_to_mcn | numeric | YES | None
cabi_trip_dist_avg_arl_to_mcs | numeric | YES | None
cabi_trip_dist_avg_arl_to_wdc | numeric | YES | None
cabi_trip_dist_avg_ffx_to_alx | numeric | YES | None
cabi_trip_dist_avg_ffx_to_arl | numeric | YES | None
cabi_trip_dist_avg_ffx_to_ffx | numeric | YES | None
cabi_trip_dist_avg_ffx_to_mcs | numeric | YES | None
cabi_trip_dist_avg_ffx_to_wdc | numeric | YES | None
cabi_trip_dist_avg_mcn_to_arl | numeric | YES | None
cabi_trip_dist_avg_mcn_to_mcn | numeric | YES | None
cabi_trip_dist_avg_mcn_to_mcs | numeric | YES | None
cabi_trip_dist_avg_mcn_to_wdc | numeric | YES | None
cabi_trip_dist_avg_mcs_to_alx | numeric | YES | None
cabi_trip_dist_avg_mcs_to_arl | numeric | YES | None
cabi_trip_dist_avg_mcs_to_ffx | numeric | YES | None
cabi_trip_dist_avg_mcs_to_mcn | numeric | YES | None
cabi_trip_dist_avg_mcs_to_mcs | numeric | YES | None
cabi_trip_dist_avg_mcs_to_wdc | numeric | YES | None
cabi_trip_dist_avg_wdc_to_alx | numeric | YES | None
cabi_trip_dist_avg_wdc_to_arl | numeric | YES | None
cabi_trip_dist_avg_wdc_to_ffx | numeric | YES | None
cabi_trip_dist_avg_wdc_to_mcn | numeric | YES | None
cabi_trip_dist_avg_wdc_to_mcs | numeric | YES | None
cabi_trip_dist_avg_wdc_to_wdc | numeric | YES | None
cabi_trip_cost_avg_alx_to_alx | numeric | YES | None
cabi_trip_cost_avg_alx_to_arl | numeric | YES | None
cabi_trip_cost_avg_alx_to_ffx | numeric | YES | None
cabi_trip_cost_avg_alx_to_mcn | numeric | YES | None
cabi_trip_cost_avg_alx_to_mcs | numeric | YES | None
cabi_trip_cost_avg_alx_to_wdc | numeric | YES | None
cabi_trip_cost_avg_arl_to_alx | numeric | YES | None
cabi_trip_cost_avg_arl_to_arl | numeric | YES | None
cabi_trip_cost_avg_arl_to_ffx | numeric | YES | None
cabi_trip_cost_avg_arl_to_mcn | numeric | YES | None
cabi_trip_cost_avg_arl_to_mcs | numeric | YES | None
cabi_trip_cost_avg_arl_to_wdc | numeric | YES | None
cabi_trip_cost_avg_ffx_to_alx | numeric | YES | None
cabi_trip_cost_avg_ffx_to_arl | numeric | YES | None
cabi_trip_cost_avg_ffx_to_ffx | numeric | YES | None
cabi_trip_cost_avg_ffx_to_mcs | numeric | YES | None
cabi_trip_cost_avg_ffx_to_wdc | numeric | YES | None
cabi_trip_cost_avg_mcn_to_arl | numeric | YES | None
cabi_trip_cost_avg_mcn_to_mcn | numeric | YES | None
cabi_trip_cost_avg_mcn_to_mcs | numeric | YES | None
cabi_trip_cost_avg_mcn_to_wdc | numeric | YES | None
cabi_trip_cost_avg_mcs_to_alx | numeric | YES | None
cabi_trip_cost_avg_mcs_to_arl | numeric | YES | None
cabi_trip_cost_avg_mcs_to_ffx | numeric | YES | None
cabi_trip_cost_avg_mcs_to_mcn | numeric | YES | None
cabi_trip_cost_avg_mcs_to_mcs | numeric | YES | None
cabi_trip_cost_avg_mcs_to_wdc | numeric | YES | None
cabi_trip_cost_avg_wdc_to_alx | numeric | YES | None
cabi_trip_cost_avg_wdc_to_arl | numeric | YES | None
cabi_trip_cost_avg_wdc_to_ffx | numeric | YES | None
cabi_trip_cost_avg_wdc_to_mcn | numeric | YES | None
cabi_trip_cost_avg_wdc_to_mcs | numeric | YES | None
cabi_trip_cost_avg_wdc_to_wdc | numeric | YES | None
cabi_trips_arl_to_arl_casual | numeric | YES | None
cabi_trips_arl_to_arl_member | numeric | YES | None
cabi_trips_wdc_to_arl_member | numeric | YES | None
cabi_trips_wdc_to_wdc_casual | numeric | YES | None
cabi_trips_wdc_to_wdc_member | numeric | YES | None
cabi_trips_arl_to_wdc_casual | numeric | YES | None
cabi_trips_arl_to_wdc_member | numeric | YES | None
cabi_trips_wdc_to_arl_casual | numeric | YES | None
cabi_trips_wdc_to_wdc_unknown | numeric | YES | None
cabi_trips_arl_to_arl_unknown | numeric | YES | None
cabi_trips_alx_to_alx_member | numeric | YES | None
cabi_trips_alx_to_alx_casual | numeric | YES | None
cabi_trips_alx_to_arl_member | numeric | YES | None
cabi_trips_arl_to_alx_member | numeric | YES | None
cabi_trips_alx_to_arl_casual | numeric | YES | None
cabi_trips_alx_to_wdc_member | numeric | YES | None
cabi_trips_arl_to_alx_casual | numeric | YES | None
cabi_trips_wdc_to_alx_casual | numeric | YES | None
cabi_trips_wdc_to_alx_member | numeric | YES | None
cabi_trips_alx_to_wdc_casual | numeric | YES | None
cabi_trips_mcs_to_wdc_member | numeric | YES | None
cabi_trips_wdc_to_mcs_member | numeric | YES | None
cabi_trips_mcs_to_wdc_casual | numeric | YES | None
cabi_trips_wdc_to_mcs_casual | numeric | YES | None
cabi_trips_mcs_to_mcs_casual | numeric | YES | None
cabi_trips_mcs_to_mcs_member | numeric | YES | None
cabi_trips_mcs_to_arl_member | numeric | YES | None
cabi_trips_mcs_to_arl_casual | numeric | YES | None
cabi_trips_arl_to_mcs_casual | numeric | YES | None
cabi_trips_mcn_to_mcn_member | numeric | YES | None
cabi_trips_mcn_to_mcn_casual | numeric | YES | None
cabi_trips_mcn_to_mcs_member | numeric | YES | None
cabi_trips_mcs_to_mcn_member | numeric | YES | None
cabi_trips_mcn_to_wdc_casual | numeric | YES | None
cabi_trips_arl_to_mcs_member | numeric | YES | None
cabi_trips_wdc_to_mcn_member | numeric | YES | None
cabi_trips_mcs_to_mcn_casual | numeric | YES | None
cabi_trips_wdc_to_mcn_casual | numeric | YES | None
cabi_trips_mcs_to_alx_casual | numeric | YES | None
cabi_trips_mcn_to_mcs_casual | numeric | YES | None
cabi_trips_mcn_to_wdc_member | numeric | YES | None
cabi_trips_alx_to_mcs_casual | numeric | YES | None
cabi_trips_mcs_to_alx_member | numeric | YES | None
cabi_trips_wdc_to_arl_unknown | numeric | YES | None
cabi_trips_alx_to_mcs_member | numeric | YES | None
cabi_trips_arl_to_mcn_casual | numeric | YES | None
cabi_trips_alx_to_mcn_casual | numeric | YES | None
cabi_trips_arl_to_mcn_member | numeric | YES | None
cabi_trips_alx_to_mcn_member | numeric | YES | None
cabi_trips_ffx_to_ffx_member | numeric | YES | None
cabi_trips_ffx_to_ffx_casual | numeric | YES | None
cabi_trips_ffx_to_wdc_member | numeric | YES | None
cabi_trips_ffx_to_arl_member | numeric | YES | None
cabi_trips_ffx_to_mcs_member | numeric | YES | None
cabi_trips_mcn_to_arl_casual | numeric | YES | None
cabi_trips_ffx_to_wdc_casual | numeric | YES | None
cabi_trips_ffx_to_arl_casual | numeric | YES | None
cabi_trips_arl_to_ffx_member | numeric | YES | None
cabi_trips_alx_to_ffx_casual | numeric | YES | None
cabi_trips_wdc_to_ffx_casual | numeric | YES | None
cabi_trips_arl_to_ffx_casual | numeric | YES | None
cabi_trips_wdc_to_ffx_member | numeric | YES | None
cabi_trips_ffx_to_alx_casual | numeric | YES | None
cabi_trips_mcs_to_ffx_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_arl_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_arl_member | numeric | YES | None
cabi_trip_dur_tot_wdc_to_arl_member | numeric | YES | None
cabi_trip_dur_tot_wdc_to_wdc_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_wdc_member | numeric | YES | None
cabi_trip_dur_tot_arl_to_wdc_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_wdc_member | numeric | YES | None
cabi_trip_dur_tot_wdc_to_arl_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_wdc_unknown | numeric | YES | None
cabi_trip_dur_tot_arl_to_arl_unknown | numeric | YES | None
cabi_trip_dur_tot_alx_to_alx_member | numeric | YES | None
cabi_trip_dur_tot_alx_to_alx_casual | numeric | YES | None
cabi_trip_dur_tot_alx_to_arl_member | numeric | YES | None
cabi_trip_dur_tot_arl_to_alx_member | numeric | YES | None
cabi_trip_dur_tot_alx_to_arl_casual | numeric | YES | None
cabi_trip_dur_tot_alx_to_wdc_member | numeric | YES | None
cabi_trip_dur_tot_arl_to_alx_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_alx_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_alx_member | numeric | YES | None
cabi_trip_dur_tot_alx_to_wdc_casual | numeric | YES | None
cabi_trip_dur_tot_mcs_to_wdc_member | numeric | YES | None
cabi_trip_dur_tot_wdc_to_mcs_member | numeric | YES | None
cabi_trip_dur_tot_mcs_to_wdc_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_mcs_casual | numeric | YES | None
cabi_trip_dur_tot_mcs_to_mcs_casual | numeric | YES | None
cabi_trip_dur_tot_mcs_to_mcs_member | numeric | YES | None
cabi_trip_dur_tot_mcs_to_arl_member | numeric | YES | None
cabi_trip_dur_tot_mcs_to_arl_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_mcs_casual | numeric | YES | None
cabi_trip_dur_tot_mcn_to_mcn_member | numeric | YES | None
cabi_trip_dur_tot_mcn_to_mcn_casual | numeric | YES | None
cabi_trip_dur_tot_mcn_to_mcs_member | numeric | YES | None
cabi_trip_dur_tot_mcs_to_mcn_member | numeric | YES | None
cabi_trip_dur_tot_mcn_to_wdc_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_mcs_member | numeric | YES | None
cabi_trip_dur_tot_wdc_to_mcn_member | numeric | YES | None
cabi_trip_dur_tot_mcs_to_mcn_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_mcn_casual | numeric | YES | None
cabi_trip_dur_tot_mcs_to_alx_casual | numeric | YES | None
cabi_trip_dur_tot_mcn_to_mcs_casual | numeric | YES | None
cabi_trip_dur_tot_mcn_to_wdc_member | numeric | YES | None
cabi_trip_dur_tot_alx_to_mcs_casual | numeric | YES | None
cabi_trip_dur_tot_mcs_to_alx_member | numeric | YES | None
cabi_trip_dur_tot_wdc_to_arl_unknown | numeric | YES | None
cabi_trip_dur_tot_alx_to_mcs_member | numeric | YES | None
cabi_trip_dur_tot_arl_to_mcn_casual | numeric | YES | None
cabi_trip_dur_tot_alx_to_mcn_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_mcn_member | numeric | YES | None
cabi_trip_dur_tot_alx_to_mcn_member | numeric | YES | None
cabi_trip_dur_tot_ffx_to_ffx_member | numeric | YES | None
cabi_trip_dur_tot_ffx_to_ffx_casual | numeric | YES | None
cabi_trip_dur_tot_ffx_to_wdc_member | numeric | YES | None
cabi_trip_dur_tot_ffx_to_arl_member | numeric | YES | None
cabi_trip_dur_tot_ffx_to_mcs_member | numeric | YES | None
cabi_trip_dur_tot_mcn_to_arl_casual | numeric | YES | None
cabi_trip_dur_tot_ffx_to_wdc_casual | numeric | YES | None
cabi_trip_dur_tot_ffx_to_arl_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_ffx_member | numeric | YES | None
cabi_trip_dur_tot_alx_to_ffx_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_ffx_casual | numeric | YES | None
cabi_trip_dur_tot_arl_to_ffx_casual | numeric | YES | None
cabi_trip_dur_tot_wdc_to_ffx_member | numeric | YES | None
cabi_trip_dur_tot_ffx_to_alx_casual | numeric | YES | None
cabi_trip_dur_tot_mcs_to_ffx_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_arl_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_arl_member | numeric | YES | None
cabi_trip_dist_tot_wdc_to_arl_member | numeric | YES | None
cabi_trip_dist_tot_wdc_to_wdc_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_wdc_member | numeric | YES | None
cabi_trip_dist_tot_arl_to_wdc_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_wdc_member | numeric | YES | None
cabi_trip_dist_tot_wdc_to_arl_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_wdc_unknown | numeric | YES | None
cabi_trip_dist_tot_arl_to_arl_unknown | numeric | YES | None
cabi_trip_dist_tot_alx_to_alx_member | numeric | YES | None
cabi_trip_dist_tot_alx_to_alx_casual | numeric | YES | None
cabi_trip_dist_tot_alx_to_arl_member | numeric | YES | None
cabi_trip_dist_tot_arl_to_alx_member | numeric | YES | None
cabi_trip_dist_tot_alx_to_arl_casual | numeric | YES | None
cabi_trip_dist_tot_alx_to_wdc_member | numeric | YES | None
cabi_trip_dist_tot_arl_to_alx_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_alx_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_alx_member | numeric | YES | None
cabi_trip_dist_tot_alx_to_wdc_casual | numeric | YES | None
cabi_trip_dist_tot_mcs_to_wdc_member | numeric | YES | None
cabi_trip_dist_tot_wdc_to_mcs_member | numeric | YES | None
cabi_trip_dist_tot_mcs_to_wdc_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_mcs_casual | numeric | YES | None
cabi_trip_dist_tot_mcs_to_mcs_casual | numeric | YES | None
cabi_trip_dist_tot_mcs_to_mcs_member | numeric | YES | None
cabi_trip_dist_tot_mcs_to_arl_member | numeric | YES | None
cabi_trip_dist_tot_mcs_to_arl_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_mcs_casual | numeric | YES | None
cabi_trip_dist_tot_mcn_to_mcn_member | numeric | YES | None
cabi_trip_dist_tot_mcn_to_mcn_casual | numeric | YES | None
cabi_trip_dist_tot_mcn_to_mcs_member | numeric | YES | None
cabi_trip_dist_tot_mcs_to_mcn_member | numeric | YES | None
cabi_trip_dist_tot_mcn_to_wdc_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_mcs_member | numeric | YES | None
cabi_trip_dist_tot_wdc_to_mcn_member | numeric | YES | None
cabi_trip_dist_tot_mcs_to_mcn_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_mcn_casual | numeric | YES | None
cabi_trip_dist_tot_mcs_to_alx_casual | numeric | YES | None
cabi_trip_dist_tot_mcn_to_mcs_casual | numeric | YES | None
cabi_trip_dist_tot_mcn_to_wdc_member | numeric | YES | None
cabi_trip_dist_tot_alx_to_mcs_casual | numeric | YES | None
cabi_trip_dist_tot_mcs_to_alx_member | numeric | YES | None
cabi_trip_dist_tot_wdc_to_arl_unknown | numeric | YES | None
cabi_trip_dist_tot_alx_to_mcs_member | numeric | YES | None
cabi_trip_dist_tot_arl_to_mcn_casual | numeric | YES | None
cabi_trip_dist_tot_alx_to_mcn_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_mcn_member | numeric | YES | None
cabi_trip_dist_tot_alx_to_mcn_member | numeric | YES | None
cabi_trip_dist_tot_ffx_to_ffx_member | numeric | YES | None
cabi_trip_dist_tot_ffx_to_ffx_casual | numeric | YES | None
cabi_trip_dist_tot_ffx_to_wdc_member | numeric | YES | None
cabi_trip_dist_tot_ffx_to_arl_member | numeric | YES | None
cabi_trip_dist_tot_ffx_to_mcs_member | numeric | YES | None
cabi_trip_dist_tot_mcn_to_arl_casual | numeric | YES | None
cabi_trip_dist_tot_ffx_to_wdc_casual | numeric | YES | None
cabi_trip_dist_tot_ffx_to_arl_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_ffx_member | numeric | YES | None
cabi_trip_dist_tot_alx_to_ffx_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_ffx_casual | numeric | YES | None
cabi_trip_dist_tot_arl_to_ffx_casual | numeric | YES | None
cabi_trip_dist_tot_wdc_to_ffx_member | numeric | YES | None
cabi_trip_dist_tot_ffx_to_alx_casual | numeric | YES | None
cabi_trip_dist_tot_mcs_to_ffx_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_arl_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_arl_member | numeric | YES | None
cabi_trip_cost_tot_wdc_to_arl_member | numeric | YES | None
cabi_trip_cost_tot_wdc_to_wdc_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_wdc_member | numeric | YES | None
cabi_trip_cost_tot_arl_to_wdc_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_wdc_member | numeric | YES | None
cabi_trip_cost_tot_wdc_to_arl_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_wdc_unknown | numeric | YES | None
cabi_trip_cost_tot_arl_to_arl_unknown | numeric | YES | None
cabi_trip_cost_tot_alx_to_alx_member | numeric | YES | None
cabi_trip_cost_tot_alx_to_alx_casual | numeric | YES | None
cabi_trip_cost_tot_alx_to_arl_member | numeric | YES | None
cabi_trip_cost_tot_arl_to_alx_member | numeric | YES | None
cabi_trip_cost_tot_alx_to_arl_casual | numeric | YES | None
cabi_trip_cost_tot_alx_to_wdc_member | numeric | YES | None
cabi_trip_cost_tot_arl_to_alx_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_alx_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_alx_member | numeric | YES | None
cabi_trip_cost_tot_alx_to_wdc_casual | numeric | YES | None
cabi_trip_cost_tot_mcs_to_wdc_member | numeric | YES | None
cabi_trip_cost_tot_wdc_to_mcs_member | numeric | YES | None
cabi_trip_cost_tot_mcs_to_wdc_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_mcs_casual | numeric | YES | None
cabi_trip_cost_tot_mcs_to_mcs_casual | numeric | YES | None
cabi_trip_cost_tot_mcs_to_mcs_member | numeric | YES | None
cabi_trip_cost_tot_mcs_to_arl_member | numeric | YES | None
cabi_trip_cost_tot_mcs_to_arl_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_mcs_casual | numeric | YES | None
cabi_trip_cost_tot_mcn_to_mcn_member | numeric | YES | None
cabi_trip_cost_tot_mcn_to_mcn_casual | numeric | YES | None
cabi_trip_cost_tot_mcn_to_mcs_member | numeric | YES | None
cabi_trip_cost_tot_mcs_to_mcn_member | numeric | YES | None
cabi_trip_cost_tot_mcn_to_wdc_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_mcs_member | numeric | YES | None
cabi_trip_cost_tot_wdc_to_mcn_member | numeric | YES | None
cabi_trip_cost_tot_mcs_to_mcn_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_mcn_casual | numeric | YES | None
cabi_trip_cost_tot_mcs_to_alx_casual | numeric | YES | None
cabi_trip_cost_tot_mcn_to_mcs_casual | numeric | YES | None
cabi_trip_cost_tot_mcn_to_wdc_member | numeric | YES | None
cabi_trip_cost_tot_alx_to_mcs_casual | numeric | YES | None
cabi_trip_cost_tot_mcs_to_alx_member | numeric | YES | None
cabi_trip_cost_tot_wdc_to_arl_unknown | numeric | YES | None
cabi_trip_cost_tot_alx_to_mcs_member | numeric | YES | None
cabi_trip_cost_tot_arl_to_mcn_casual | numeric | YES | None
cabi_trip_cost_tot_alx_to_mcn_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_mcn_member | numeric | YES | None
cabi_trip_cost_tot_alx_to_mcn_member | numeric | YES | None
cabi_trip_cost_tot_ffx_to_ffx_member | numeric | YES | None
cabi_trip_cost_tot_ffx_to_ffx_casual | numeric | YES | None
cabi_trip_cost_tot_ffx_to_wdc_member | numeric | YES | None
cabi_trip_cost_tot_ffx_to_arl_member | numeric | YES | None
cabi_trip_cost_tot_ffx_to_mcs_member | numeric | YES | None
cabi_trip_cost_tot_mcn_to_arl_casual | numeric | YES | None
cabi_trip_cost_tot_ffx_to_wdc_casual | numeric | YES | None
cabi_trip_cost_tot_ffx_to_arl_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_ffx_member | numeric | YES | None
cabi_trip_cost_tot_alx_to_ffx_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_ffx_casual | numeric | YES | None
cabi_trip_cost_tot_arl_to_ffx_casual | numeric | YES | None
cabi_trip_cost_tot_wdc_to_ffx_member | numeric | YES | None
cabi_trip_cost_tot_ffx_to_alx_casual | numeric | YES | None
cabi_trip_cost_tot_mcs_to_ffx_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_arl_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_arl_member | numeric | YES | None
cabi_trip_dur_avg_wdc_to_arl_member | numeric | YES | None
cabi_trip_dur_avg_wdc_to_wdc_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_wdc_member | numeric | YES | None
cabi_trip_dur_avg_arl_to_wdc_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_wdc_member | numeric | YES | None
cabi_trip_dur_avg_wdc_to_arl_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_wdc_unknown | numeric | YES | None
cabi_trip_dur_avg_arl_to_arl_unknown | numeric | YES | None
cabi_trip_dur_avg_alx_to_alx_member | numeric | YES | None
cabi_trip_dur_avg_alx_to_alx_casual | numeric | YES | None
cabi_trip_dur_avg_alx_to_arl_member | numeric | YES | None
cabi_trip_dur_avg_arl_to_alx_member | numeric | YES | None
cabi_trip_dur_avg_alx_to_arl_casual | numeric | YES | None
cabi_trip_dur_avg_alx_to_wdc_member | numeric | YES | None
cabi_trip_dur_avg_arl_to_alx_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_alx_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_alx_member | numeric | YES | None
cabi_trip_dur_avg_alx_to_wdc_casual | numeric | YES | None
cabi_trip_dur_avg_mcs_to_wdc_member | numeric | YES | None
cabi_trip_dur_avg_wdc_to_mcs_member | numeric | YES | None
cabi_trip_dur_avg_mcs_to_wdc_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_mcs_casual | numeric | YES | None
cabi_trip_dur_avg_mcs_to_mcs_casual | numeric | YES | None
cabi_trip_dur_avg_mcs_to_mcs_member | numeric | YES | None
cabi_trip_dur_avg_mcs_to_arl_member | numeric | YES | None
cabi_trip_dur_avg_mcs_to_arl_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_mcs_casual | numeric | YES | None
cabi_trip_dur_avg_mcn_to_mcn_member | numeric | YES | None
cabi_trip_dur_avg_mcn_to_mcn_casual | numeric | YES | None
cabi_trip_dur_avg_mcn_to_mcs_member | numeric | YES | None
cabi_trip_dur_avg_mcs_to_mcn_member | numeric | YES | None
cabi_trip_dur_avg_mcn_to_wdc_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_mcs_member | numeric | YES | None
cabi_trip_dur_avg_wdc_to_mcn_member | numeric | YES | None
cabi_trip_dur_avg_mcs_to_mcn_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_mcn_casual | numeric | YES | None
cabi_trip_dur_avg_mcs_to_alx_casual | numeric | YES | None
cabi_trip_dur_avg_mcn_to_mcs_casual | numeric | YES | None
cabi_trip_dur_avg_mcn_to_wdc_member | numeric | YES | None
cabi_trip_dur_avg_alx_to_mcs_casual | numeric | YES | None
cabi_trip_dur_avg_mcs_to_alx_member | numeric | YES | None
cabi_trip_dur_avg_wdc_to_arl_unknown | numeric | YES | None
cabi_trip_dur_avg_alx_to_mcs_member | numeric | YES | None
cabi_trip_dur_avg_arl_to_mcn_casual | numeric | YES | None
cabi_trip_dur_avg_alx_to_mcn_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_mcn_member | numeric | YES | None
cabi_trip_dur_avg_alx_to_mcn_member | numeric | YES | None
cabi_trip_dur_avg_ffx_to_ffx_member | numeric | YES | None
cabi_trip_dur_avg_ffx_to_ffx_casual | numeric | YES | None
cabi_trip_dur_avg_ffx_to_wdc_member | numeric | YES | None
cabi_trip_dur_avg_ffx_to_arl_member | numeric | YES | None
cabi_trip_dur_avg_ffx_to_mcs_member | numeric | YES | None
cabi_trip_dur_avg_mcn_to_arl_casual | numeric | YES | None
cabi_trip_dur_avg_ffx_to_wdc_casual | numeric | YES | None
cabi_trip_dur_avg_ffx_to_arl_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_ffx_member | numeric | YES | None
cabi_trip_dur_avg_alx_to_ffx_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_ffx_casual | numeric | YES | None
cabi_trip_dur_avg_arl_to_ffx_casual | numeric | YES | None
cabi_trip_dur_avg_wdc_to_ffx_member | numeric | YES | None
cabi_trip_dur_avg_ffx_to_alx_casual | numeric | YES | None
cabi_trip_dur_avg_mcs_to_ffx_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_arl_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_arl_member | numeric | YES | None
cabi_trip_dist_avg_wdc_to_arl_member | numeric | YES | None
cabi_trip_dist_avg_wdc_to_wdc_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_wdc_member | numeric | YES | None
cabi_trip_dist_avg_arl_to_wdc_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_wdc_member | numeric | YES | None
cabi_trip_dist_avg_wdc_to_arl_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_wdc_unknown | numeric | YES | None
cabi_trip_dist_avg_arl_to_arl_unknown | numeric | YES | None
cabi_trip_dist_avg_alx_to_alx_member | numeric | YES | None
cabi_trip_dist_avg_alx_to_alx_casual | numeric | YES | None
cabi_trip_dist_avg_alx_to_arl_member | numeric | YES | None
cabi_trip_dist_avg_arl_to_alx_member | numeric | YES | None
cabi_trip_dist_avg_alx_to_arl_casual | numeric | YES | None
cabi_trip_dist_avg_alx_to_wdc_member | numeric | YES | None
cabi_trip_dist_avg_arl_to_alx_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_alx_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_alx_member | numeric | YES | None
cabi_trip_dist_avg_alx_to_wdc_casual | numeric | YES | None
cabi_trip_dist_avg_mcs_to_wdc_member | numeric | YES | None
cabi_trip_dist_avg_wdc_to_mcs_member | numeric | YES | None
cabi_trip_dist_avg_mcs_to_wdc_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_mcs_casual | numeric | YES | None
cabi_trip_dist_avg_mcs_to_mcs_casual | numeric | YES | None
cabi_trip_dist_avg_mcs_to_mcs_member | numeric | YES | None
cabi_trip_dist_avg_mcs_to_arl_member | numeric | YES | None
cabi_trip_dist_avg_mcs_to_arl_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_mcs_casual | numeric | YES | None
cabi_trip_dist_avg_mcn_to_mcn_member | numeric | YES | None
cabi_trip_dist_avg_mcn_to_mcn_casual | numeric | YES | None
cabi_trip_dist_avg_mcn_to_mcs_member | numeric | YES | None
cabi_trip_dist_avg_mcs_to_mcn_member | numeric | YES | None
cabi_trip_dist_avg_mcn_to_wdc_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_mcs_member | numeric | YES | None
cabi_trip_dist_avg_wdc_to_mcn_member | numeric | YES | None
cabi_trip_dist_avg_mcs_to_mcn_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_mcn_casual | numeric | YES | None
cabi_trip_dist_avg_mcs_to_alx_casual | numeric | YES | None
cabi_trip_dist_avg_mcn_to_mcs_casual | numeric | YES | None
cabi_trip_dist_avg_mcn_to_wdc_member | numeric | YES | None
cabi_trip_dist_avg_alx_to_mcs_casual | numeric | YES | None
cabi_trip_dist_avg_mcs_to_alx_member | numeric | YES | None
cabi_trip_dist_avg_wdc_to_arl_unknown | numeric | YES | None
cabi_trip_dist_avg_alx_to_mcs_member | numeric | YES | None
cabi_trip_dist_avg_arl_to_mcn_casual | numeric | YES | None
cabi_trip_dist_avg_alx_to_mcn_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_mcn_member | numeric | YES | None
cabi_trip_dist_avg_alx_to_mcn_member | numeric | YES | None
cabi_trip_dist_avg_ffx_to_ffx_member | numeric | YES | None
cabi_trip_dist_avg_ffx_to_ffx_casual | numeric | YES | None
cabi_trip_dist_avg_ffx_to_wdc_member | numeric | YES | None
cabi_trip_dist_avg_ffx_to_arl_member | numeric | YES | None
cabi_trip_dist_avg_ffx_to_mcs_member | numeric | YES | None
cabi_trip_dist_avg_mcn_to_arl_casual | numeric | YES | None
cabi_trip_dist_avg_ffx_to_wdc_casual | numeric | YES | None
cabi_trip_dist_avg_ffx_to_arl_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_ffx_member | numeric | YES | None
cabi_trip_dist_avg_alx_to_ffx_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_ffx_casual | numeric | YES | None
cabi_trip_dist_avg_arl_to_ffx_casual | numeric | YES | None
cabi_trip_dist_avg_wdc_to_ffx_member | numeric | YES | None
cabi_trip_dist_avg_ffx_to_alx_casual | numeric | YES | None
cabi_trip_dist_avg_mcs_to_ffx_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_arl_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_arl_member | numeric | YES | None
cabi_trip_cost_avg_wdc_to_arl_member | numeric | YES | None
cabi_trip_cost_avg_wdc_to_wdc_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_wdc_member | numeric | YES | None
cabi_trip_cost_avg_arl_to_wdc_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_wdc_member | numeric | YES | None
cabi_trip_cost_avg_wdc_to_arl_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_wdc_unknown | numeric | YES | None
cabi_trip_cost_avg_arl_to_arl_unknown | numeric | YES | None
cabi_trip_cost_avg_alx_to_alx_member | numeric | YES | None
cabi_trip_cost_avg_alx_to_alx_casual | numeric | YES | None
cabi_trip_cost_avg_alx_to_arl_member | numeric | YES | None
cabi_trip_cost_avg_arl_to_alx_member | numeric | YES | None
cabi_trip_cost_avg_alx_to_arl_casual | numeric | YES | None
cabi_trip_cost_avg_alx_to_wdc_member | numeric | YES | None
cabi_trip_cost_avg_arl_to_alx_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_alx_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_alx_member | numeric | YES | None
cabi_trip_cost_avg_alx_to_wdc_casual | numeric | YES | None
cabi_trip_cost_avg_mcs_to_wdc_member | numeric | YES | None
cabi_trip_cost_avg_wdc_to_mcs_member | numeric | YES | None
cabi_trip_cost_avg_mcs_to_wdc_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_mcs_casual | numeric | YES | None
cabi_trip_cost_avg_mcs_to_mcs_casual | numeric | YES | None
cabi_trip_cost_avg_mcs_to_mcs_member | numeric | YES | None
cabi_trip_cost_avg_mcs_to_arl_member | numeric | YES | None
cabi_trip_cost_avg_mcs_to_arl_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_mcs_casual | numeric | YES | None
cabi_trip_cost_avg_mcn_to_mcn_member | numeric | YES | None
cabi_trip_cost_avg_mcn_to_mcn_casual | numeric | YES | None
cabi_trip_cost_avg_mcn_to_mcs_member | numeric | YES | None
cabi_trip_cost_avg_mcs_to_mcn_member | numeric | YES | None
cabi_trip_cost_avg_mcn_to_wdc_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_mcs_member | numeric | YES | None
cabi_trip_cost_avg_wdc_to_mcn_member | numeric | YES | None
cabi_trip_cost_avg_mcs_to_mcn_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_mcn_casual | numeric | YES | None
cabi_trip_cost_avg_mcs_to_alx_casual | numeric | YES | None
cabi_trip_cost_avg_mcn_to_mcs_casual | numeric | YES | None
cabi_trip_cost_avg_mcn_to_wdc_member | numeric | YES | None
cabi_trip_cost_avg_alx_to_mcs_casual | numeric | YES | None
cabi_trip_cost_avg_mcs_to_alx_member | numeric | YES | None
cabi_trip_cost_avg_wdc_to_arl_unknown | numeric | YES | None
cabi_trip_cost_avg_alx_to_mcs_member | numeric | YES | None
cabi_trip_cost_avg_arl_to_mcn_casual | numeric | YES | None
cabi_trip_cost_avg_alx_to_mcn_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_mcn_member | numeric | YES | None
cabi_trip_cost_avg_alx_to_mcn_member | numeric | YES | None
cabi_trip_cost_avg_ffx_to_ffx_member | numeric | YES | None
cabi_trip_cost_avg_ffx_to_ffx_casual | numeric | YES | None
cabi_trip_cost_avg_ffx_to_wdc_member | numeric | YES | None
cabi_trip_cost_avg_ffx_to_arl_member | numeric | YES | None
cabi_trip_cost_avg_ffx_to_mcs_member | numeric | YES | None
cabi_trip_cost_avg_mcn_to_arl_casual | numeric | YES | None
cabi_trip_cost_avg_ffx_to_wdc_casual | numeric | YES | None
cabi_trip_cost_avg_ffx_to_arl_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_ffx_member | numeric | YES | None
cabi_trip_cost_avg_alx_to_ffx_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_ffx_casual | numeric | YES | None
cabi_trip_cost_avg_arl_to_ffx_casual | numeric | YES | None
cabi_trip_cost_avg_wdc_to_ffx_member | numeric | YES | None
cabi_trip_cost_avg_ffx_to_alx_casual | numeric | YES | None
cabi_trip_cost_avg_mcs_to_ffx_casual | numeric | YES | None
cabi_bikes_avail | numeric | YES | None
cabi_stations_alx | numeric | YES | None
cabi_stations_arl | numeric | YES | None
cabi_stations_ffx | numeric | YES | None
cabi_stations_mcn | numeric | YES | None
cabi_stations_mcs | numeric | YES | None
cabi_stations_wdc | numeric | YES | None
cabi_docks_alx | numeric | YES | None
cabi_docks_arl | numeric | YES | None
cabi_docks_ffx | numeric | YES | None
cabi_docks_mcn | numeric | YES | None
cabi_docks_mcs | numeric | YES | None
cabi_docks_wdc | numeric | YES | None
cabi_stations_tot | numeric | YES | None
cabi_docks_tot | numeric | YES | None
cabi_dur_empty_wdc | numeric | YES | None
cabi_dur_full_wdc | numeric | YES | None
cabi_dur_empty_arl | numeric | YES | None
cabi_dur_full_arl | numeric | YES | None
cabi_dur_full_alx | numeric | YES | None
cabi_dur_empty_alx | numeric | YES | None
cabi_dur_empty_mcs | numeric | YES | None
cabi_dur_full_mcs | numeric | YES | None
cabi_dur_full_mcn | numeric | YES | None
cabi_dur_empty_mcn | numeric | YES | None
cabi_dur_full_ffx | numeric | YES | None
cabi_dur_empty_ffx | numeric | YES | None
cabi_dur_empty_tot | numeric | YES | None
cabi_dur_full_tot | numeric | YES | None
cabi_active_members_day_key | numeric | YES | None
cabi_active_members_monthly | numeric | YES | None
cabi_active_members_annual | numeric | YES | None
cabi_monthly_multi_day_pases | numeric | YES | None
cabi_monthly_single_day_pases | numeric | YES | None
cabi_monthly_single_trip_pases | numeric | YES | None
cabi_util_rate | numeric | YES | None
dless_trips_jump | numeric | YES | None
dless_trips_lime | numeric | YES | None
dless_trips_mobike | numeric | YES | None
dless_trips_ofo | numeric | YES | None
dless_trips_spin | numeric | YES | None
dless_trips_all | numeric | YES | None
dless_tripdist_tot_jump | numeric | YES | None
dless_tripdist_tot_lime | numeric | YES | None
dless_tripdist_tot_mobike | numeric | YES | None
dless_tripdist_tot_ofo | numeric | YES | None
dless_tripdist_tot_spin | numeric | YES | None
dless_tripdist_tot_all | numeric | YES | None
dless_tripdist_avg_jump | numeric | YES | None
dless_tripdist_avg_lime | numeric | YES | None
dless_tripdist_avg_mobike | numeric | YES | None
dless_tripdist_avg_ofo | numeric | YES | None
dless_tripdist_avg_spin | numeric | YES | None
dless_geo_start_lime | numeric | YES | None
dless_geo_start_mobike | numeric | YES | None
dless_geo_start_ofo | numeric | YES | None
dless_geo_start_spin | numeric | YES | None
dless_geo_end_lime | numeric | YES | None
dless_geo_end_mobike | numeric | YES | None
dless_geo_end_ofo | numeric | YES | None
dless_geo_end_spin | numeric | YES | None
dless_cap_start_lime | numeric | YES | None
dless_cap_start_mobike | numeric | YES | None
dless_cap_start_ofo | numeric | YES | None
dless_cap_start_spin | numeric | YES | None
dless_dur_jump | numeric | YES | None
dless_dur_lime | numeric | YES | None
dless_dur_ofo | numeric | YES | None
dless_dur_spin | numeric | YES | None
dless_cost_jump | numeric | YES | None
dless_cost_lime | numeric | YES | None
dless_cost_ofo | numeric | YES | None
dless_cost_spin | numeric | YES | None
dless_users_jump | numeric | YES | None
dless_users_lime | numeric | YES | None
dless_users_mobike | numeric | YES | None
dless_users_ofo | numeric | YES | None
dless_users_spin | numeric | YES | None
dless_bikes_jump | numeric | YES | None
dless_bikes_lime | numeric | YES | None
dless_bikes_mobike | numeric | YES | None
dless_bikes_ofo | numeric | YES | None
dless_bikes_spin | numeric | YES | None
dless_tripdist_avg_all | numeric | YES | None

**jump_price**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
min_seconds | integer | NO | None
max_seconds | integer | YES | None
cost | numeric | YES | None

**jump_users**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
userid | character varying | YES | None
trips | integer | YES | None
usage_month | date | YES | None

**nats_attendance**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
gm_num | integer | YES | None
date | date | YES | None
boxscore | character varying | YES | None
tm | character varying | YES | None
home_away | character varying | YES | None
opp | character varying | YES | None
w_or_l | character varying | YES | None
r | integer | YES | None
ra | integer | YES | None
inn | integer | YES | None
w_l_record | character varying | YES | None
rank | integer | YES | None
gb | character varying | YES | None
win | character varying | YES | None
loss | character varying | YES | None
save | character varying | YES | None
time | time without time zone | YES | None
d_n | character varying | YES | None
attendance | integer | YES | None
streak | character varying | YES | None
orig_scheduled | character varying | YES | None

**nats_games**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
game_datetime | timestamp without time zone | NO | None
game_nbr | integer | YES | None

**ngh**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
name | character varying | YES | None
nbh_names | character varying | YES | None
objectid | integer | NO | None
shape_area | numeric | YES | None
shape_length | numeric | YES | None
type | text | YES | None
web_url | character varying | YES | None
polygon | USER-DEFINED | YES | None

**ofo_users**: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
userid | character varying | YES | None
usage_month | date | YES | None
trips | integer | YES | None

