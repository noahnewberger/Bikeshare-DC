# Georgetown Capstone Team Bikeshare Data Dictionary



#### Table of Contents
* [acs](#acs): None
* [anc](#anc): DC Advisory Neighborhood Commissions converted from Open Data DC GeoJSON
* [bike_events](#bike_events): Major Bike events in the DC area 2014-2018 pulled from WABA Google Calendar
* [cabi_membership](#cabi_membership): Monthly Capital Bikeshare Membership and Pass Purchase History provided by DDOT
* [cabi_out_hist](#cabi_out_hist): History of full and empty Capital Bikeshare station events from May 2011 - March 22, 2018.  Data pulled from [cabitracker.com](http://cabitracker.com/outage_history.php)
* [cabi_price](#cabi_price): Capital Bikeshare overage pricing data for up to 24 hours of usage for both member and day pass users as of 3/25/2018.
* [cabi_stations_geo_temp](#cabi_stations_geo_temp): Capital Bikeshare station information pulled from CaBi API 3/25/2018 + geopolitical identifiers from open data DC
* [cabi_stations_temp](#cabi_stations_temp): Capital Bikeshare station information pulled from CaBi API 3/25/2018.
* [cabi_system](#cabi_system): None
* [cabi_trips](#cabi_trips): None
* [cabi_trips_membertype](#cabi_trips_membertype): None
* [dan_dockless](#dan_dockless): None
* [dark_sky_raw](#dark_sky_raw): [Dark Sky API Documentation](https://darksky.net/dev/docs)
* [dc_pop](#dc_pop): None
* [dockless_bikes_api](#dockless_bikes_api): None
* [dockless_price](#dockless_price): None
* [dockless_summary](#dockless_summary): None
* [dockless_trips](#dockless_trips): None
* [dockless_trips_geo](#dockless_trips_geo): None
* [final_db](#final_db): None
* [jump_price](#jump_price): None
* [jump_users](#jump_users): None
* [nats_attendance](#nats_attendance): None
* [nats_games](#nats_games): None
* [ngh](#ngh): None
* [ofo_users](#ofo_users): None


**acs**<a id="acs"></a>: None

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

**anc**<a id="anc"></a>: DC Advisory Neighborhood Commissions converted from Open Data DC GeoJSON

Attribute | Type | Nullable | Description
--- | --- | --- | ---
anc_id | character varying | YES | ANC name with Ward Number and ANC Letter (ie "6B")
name | character varying | YES | Same as anc_id with "ANC " concatenated prior (ie "ANC 6B")
objectid | integer | NO | ID 1 - n for each ANC, should not be used for anything
shape_area | numeric | YES | Area of the ANC in square meters
shape_length | numeric | YES | Length of the Perimeter of the ANC in meters
web_url | character varying | YES | URL to the offficial website for each ANC
polygon | USER-DEFINED | YES | List of Longitude and Latitude points that form boundary of ANC

**bike_events**<a id="bike_events"></a>: Major Bike events in the DC area 2014-2018 pulled from WABA Google Calendar

Attribute | Type | Nullable | Description
--- | --- | --- | ---
id | character varying | NO | Google Calendar Event ID
final_date | date | YES | Date of the event
summary | character varying | YES | Summary of the event per the Google Calendar description

**cabi_membership**<a id="cabi_membership"></a>: Monthly Capital Bikeshare Membership and Pass Purchase History provided by DDOT

Attribute | Type | Nullable | Description
--- | --- | --- | ---
month | date | NO | mm--yyyy (Sept 2010 - April 2018)
annual_member_purch | numeric | YES | Number of CaBi Annual Memberships Purchased per month
monthly_member_purch | numeric | YES | Number of CaBi Monthly Memberships Purchased per month
day_key_member_purch | numeric | YES | Number of CaBi Day Key Memberships Purchased per month.  Day Key are unique in that a member pays only for the days that use the key.
multi_day_pass_purch | numeric | YES | Number of CaBi 3 or 5 day passes Purchased per month
single_day_pass_purch | numeric | YES | Number of CaBi 24 hour passes Purchased per month
single_trip_pass_purch | numeric | YES | Number of CaBi Single Trips Purchased per month.  $2 Single Trips started in June 2016.

**cabi_out_hist**<a id="cabi_out_hist"></a>: History of full and empty Capital Bikeshare station events from May 2011 - March 22, 2018.  Data pulled from [cabitracker.com](http://cabitracker.com/outage_history.php)

Attribute | Type | Nullable | Description
--- | --- | --- | ---
terminal_number | character varying | YES | CaBi Station "Short Code"
status | character varying | YES | Empty/Full
start_time | timestamp without time zone | YES | Timestamp for start of status event
end_time | timestamp without time zone | YES | Timestamp for end of status event
duration | integer | YES | Duration of status in minutes (do not use)
outage_id | integer | NO | Primary key for each status event

**cabi_price**<a id="cabi_price"></a>: Capital Bikeshare overage pricing data for up to 24 hours of usage for both member and day pass users as of 3/25/2018.

Attribute | Type | Nullable | Description
--- | --- | --- | ---
min_seconds | integer | NO | Low end of time range for price in seconds up to 24 hours
max_seconds | integer | YES | High end of time range of price in seconds up to 24 hours
casual_cost | numeric | YES | Cost for Casual User
member_cost | numeric | YES | Cost  for CaBi Member

**cabi_stations_geo_temp**<a id="cabi_stations_geo_temp"></a>: Capital Bikeshare station information pulled from CaBi API 3/25/2018 + geopolitical identifiers from open data DC

Attribute | Type | Nullable | Description
--- | --- | --- | ---
start_short_name | character varying | YES | 5 Digit unique station code - Start Station
end_short_name | character varying | YES | 5 Digit unique station code - End Station
start_capacity | integer | YES | Number of Docks - Start Station
start_eightd_has_key_dispenser | boolean | YES | True/False if the station has a key dispenser - Start Station
start_lat | numeric | YES | Latitude - Start Station
start_lon | numeric | YES | Longitude - Start Station
start_name | character varying | YES | Colloquial Name of Station (ie 17th and Mass Ave NW) - Start Station
start_region_id | integer | YES | CABI jurisdictional region (ie 42=DC, 41= Arlington, VA) - Start Station
start_rental_methods | character varying | YES | List of rental payment methods available - Start Station
start_rental_url | character varying | YES | Station URL - Start Station
start_station_id | integer | YES | Foreign key - Start Station
start_region_code | character varying | YES | CABI jurisidictional region three digit code(ie WDC, ARL) - Start Station
start_cluster_name | character varying | YES | DC Neighborhood Cluster ID (ie "Cluster 1") - Start Station
start_ngh_names | character varying | YES | DC Neighborhood Cluster Name (ie ""Dupont Circle, Connecticut Avenue/K Street"") - Start Station
start_anc | character varying | YES | DC Advisory Neighborhood Commission (ie "6B")  - Start Station
start_ward | character varying | YES | DC Ward (ie "6")  - Start Station
end_capacity | integer | YES | Number of Docks - End Station
end_eightd_has_key_dispenser | boolean | YES | True/False if the station has a key dispenser - End Station
end_lat | numeric | YES | Latitude - End Station
end_lon | numeric | YES | Longitude - End Station
end_name | character varying | YES | Colloquial Name of Station (ie 17th and Mass Ave NW) - End Station
end_region_id | integer | YES | CABI jurisdictional region (ie 42=DC, 41= Arlington, VA) - End Station
end_rental_methods | character varying | YES | List of rental payment methods available - End Station
end_rental_url | character varying | YES | Station URL - End Station
end_station_id | integer | YES | Foreign key - End Station
end_region_code | character varying | YES | CABI jurisidictional region three digit code(ie WDC, ARL) - End Station
end_cluster_name | character varying | YES | DC Neighborhood Cluster ID (ie "Cluster 1") - End Station
end_ngh_names | character varying | YES | DC Neighborhood Cluster Name (ie ""Dupont Circle, Connecticut Avenue/K Street"") - End Station
end_anc | character varying | YES | DC Advisory Neighborhood Commission (ie "6B")  - End Station
end_ward | character varying | YES | DC Ward (ie "6")  - End Station
dist_miles | numeric | YES | Distance between Start and End Station in Miles

**cabi_stations_temp**<a id="cabi_stations_temp"></a>: Capital Bikeshare station information pulled from CaBi API 3/25/2018.

Attribute | Type | Nullable | Description
--- | --- | --- | ---
capacity | integer | YES | Number of Docks
eightd_has_key_dispenser | boolean | YES | True/False if the station has a key dispenser
eightd_station_services | character varying | YES | List of services available at station (ie credit card, cash, etc)
lat | numeric | YES | Latitude
lon | numeric | YES | Longitude
name | character varying | YES | Colloquial Name of Station (ie 17th and Mass Ave NW)
region_id | integer | YES | CABi justidictional region (ie 42=DC, 41= Arlington, VA)
rental_methods | character varying | YES | List of rental payment methods available
rental_url | character varying | YES | API station URL 
short_name | character varying | YES | 5 Digit unique station code
station_id | integer | NO | Primary Key

**cabi_system**<a id="cabi_system"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
region_id | integer | NO | None
name | character varying | YES | None
code | text | YES | None

**cabi_trips**<a id="cabi_trips"></a>: None

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

**cabi_trips_membertype**<a id="cabi_trips_membertype"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
startdate | timestamp without time zone | YES | None
enddate | timestamp without time zone | YES | None
bikenumber | character varying | YES | None
member_type | character varying | YES | None
trip_id | character varying | NO | None

**dan_dockless**<a id="dan_dockless"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
location_id | character varying | YES | None
location | USER-DEFINED | YES | None
provider | character varying | YES | None
bike_id | character varying | YES | None
created | timestamp without time zone | YES | None

**dark_sky_raw**<a id="dark_sky_raw"></a>: [Dark Sky API Documentation](https://darksky.net/dev/docs)

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

**dc_pop**<a id="dc_pop"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
pop_date | timestamp without time zone | NO | None
citypop | numeric | YES | None
grow_rate | numeric | YES | None
pct_bike | numeric | YES | None

**dockless_bikes_api**<a id="dockless_bikes_api"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
date | date | YES | None
operator | text | YES | None
bikes_available | integer | YES | None

**dockless_price**<a id="dockless_price"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
min_seconds | integer | NO | None
max_seconds | integer | YES | None
limebike | numeric | YES | None
spin | numeric | YES | None
ofo | numeric | YES | None
mobike | numeric | YES | None

**dockless_summary**<a id="dockless_summary"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
operator | text | YES | None
month | date | YES | None
totaltrips | numeric | YES | None
totalbikes | numeric | YES | None

**dockless_trips**<a id="dockless_trips"></a>: None

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

**dockless_trips_geo**<a id="dockless_trips_geo"></a>: None

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

**final_db**<a id="final_db"></a>: None

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
us_holiday | numeric | YES | None
nats_single | numeric | YES | None
nats_double | numeric | YES | None
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
dless_geo_start_jump | numeric | YES | None
dless_geo_start_lime | numeric | YES | None
dless_geo_start_mobike | numeric | YES | None
dless_geo_start_ofo | numeric | YES | None
dless_geo_start_spin | numeric | YES | None
dless_geo_end_jump | numeric | YES | None
dless_geo_end_lime | numeric | YES | None
dless_geo_end_mobike | numeric | YES | None
dless_geo_end_ofo | numeric | YES | None
dless_geo_end_spin | numeric | YES | None
dless_cap_start_jump | numeric | YES | None
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

**jump_price**<a id="jump_price"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
min_seconds | integer | NO | None
max_seconds | integer | YES | None
cost | numeric | YES | None

**jump_users**<a id="jump_users"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
userid | character varying | YES | None
trips | integer | YES | None
usage_month | date | YES | None

**nats_attendance**<a id="nats_attendance"></a>: None

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

**nats_games**<a id="nats_games"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
game_datetime | timestamp without time zone | NO | None
game_nbr | integer | YES | None

**ngh**<a id="ngh"></a>: None

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

**ofo_users**<a id="ofo_users"></a>: None

Attribute | Type | Nullable | Description
--- | --- | --- | ---
userid | character varying | YES | None
usage_month | date | YES | None
trips | integer | YES | None

