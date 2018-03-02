# Bikeshare-DC: Code Snippets

## This folder will serve as a library of code snippets to later be integrated into the overall system.  

## Please add a description of any code snippet to this README.

1. dark_sky.py - demo on how to pull historical weather data from Dark Sky API.  Leverages an python api wrapper called [forecastio](https://pypi.python.org/pypi/python-forecastio/) that you'll need to PIP install.

1. CaBi_Data_2015.py - demo on how to roll up CaBi historical trip data into daily counts of trips and bikes used and splits out by origin/destination and member type. There are some flaws in how the unique bikes are calculated with member type, so be careful

1. CaBi_Stations.py - demo on how to pull Capital Bikeshare station information from their API

1. download_all_cabi.py - automatically downloads all historical Capital Bikeshare data from their AWS cluster

1. jump.py, limebike.py, ofo.py, spin.py - demos access to each dockless bike service's API.  Still missing Mobike.

