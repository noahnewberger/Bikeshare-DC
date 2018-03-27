# Bikeshare-DC: Data Loads

This folder will serve as a library of data loads to AWS.  

## Primary Data (CaBi and Dockless).

1. cabi_out_hist - Capital Bikeshare station outage history from May 2011 to March 22, 2018.

1. cabi_trips - Capital Bikeshare trip history from October 2010 to December 2017.

1. cabi_system - System informatiom from the CaBi API pulled on 3/24/2018.  Used primarily for appending region_code to station information 

1. cabi_stations_temp - Capital Bikeshare station information pulled from CaBi API 3/25/2018.  Will ultimately be replaced by data from DDOT.

1. cabi_pricing_model - Capital Bikeshare overage pricing data for up to 24 hours of usage for both member and day pass users as of 3/25/2018.

1. dockless_pricing_model - Pricing data all dockless except for Jump bike for up to 24 hours of usage.

## Secondary Data (Weather, DC Population, Etc).

1. dark_sky_raw - Dark Sky API data from October 2010 to March 22, 2018.  Will be updated for rest of pilot period  at some point.

1. dark_sky_final[TODO] - dark_sky_raw + further processing

1. nats_games - List of all Nationals Home games from 2010 to 2018.  Datetime of game start, game number(for double header), and game attendance (to be added)

1. acs - American Community Survey data used to generate dc_pop

1. dc_pop - DC population estimates by year and month

1. dc_bike_events - All significant bike events based on the WABA calendar as of 3/25/2018.

1. dc_ngh_clusters - Geocoordinate polygons for the DC Neighborhood clusters


