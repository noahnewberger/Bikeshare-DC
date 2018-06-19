# DC-Bikeshare
Cohort 11 Capstone Project for the Certificate of Data Science at Georgetown University School of Continuing Studies.
_Sebastian Bautista, Travis Gervais, Noah Newberger, and Mark Sussman_

## README Contents
1. [Abstract](#abstract)
1. [NDA Explanation](#nda-explanation)
1. [Background Information](#background-information)
1. [Data Sourcing and Architecture](#data-sourcing-and-architecture)
1. [Capital Bikeshare Exploration](#capital-bikeshare-exploration)
1. [Machine Learning](#machine-learning)
1. [Acknowledgements](#acknowledgements)

## Abstract

In September 2017, the DC Department of Transportation began a dockless bikeshare pilot program. The pilot program allowed 6 different dockless bikeshare operators to enter the DC market and begin offering their services, effectively putting them in direct competition with the 7.5 year old Capital Bikeshare system. Our project seeks to analyze the dockless pilot program to determine if the introduction of dockless bikes has impacted the demand among users for Capital Bikeshare (CaBI). We accomplish this analysis by gathering data on CaBi, the dockless bikeshare operators and external factors that we believe impact the DC bikeshare demand. Using historical data on Capital Bikeshare and the external factors we create two machine learning models using Lasso and Random Forest to predict the number of Capital Bikeshare rides that we would expect to see during the first eight months of the dockless pilot program. Then we compare our models' predicted values to the actual number of rides that occurred during the pilot program to determine if our models realistically estimated the impact that the dockless bikeshare pilot program has had an impact on Capital Bikeshare.

## NDA Explanation

Please note that in order to receive data shared with the DC Department of Transportation (DDOT) by the dockless operators participating in the dockless pilot, we as a Capstone Project team, had to sign a non-disclosure agreement with DDOT.  We have presented our finding to DDOT and agreed not to share any dockless specific analysis only in our report and presentation that can only be shared with Georgetown Data Science faculty and students and not for wider distribution.

The remainder of this README will walk through our finding that were Capital Bikeshare (CaBi) specific (i.e. stopping at our machine learning models, just before explaining the potential impact of the dockless bikeshare impact on CaBi)

## Background Information

In September 2010,  Capital Bikeshare (CaBi) began operating in the Washington, DC region with 1,100 bikes and 114 stations in Washington, DC and Arlington, VA. Since then CaBi has grown to approximately 437 stations and 4,500 bikes. It has expanded its coverage to include, Alexandria, VA, Montgomery County, MD, and Fairfax County, VA. The system, which sees an average of over 10,000 trips per day, has grown to be the third largest bikeshare system currently operating in the United States.  

In September 2017, the DC department of Transportation (DDOT) began a pilot program in Washington, DC which allowed for five dockless bikeshare companies to begin operating in the city. Dockless bikeshare bikes differ notably from CaBi in that the bikes do not need to be taken from or returned to physical docking stations. Instead, the dockless bikes can be left anywhere in the city as long as they are on public property and they are not obstructing roadways or pedestrian walkways. The lack of infrastructural prerequisites meant that seemingly overnight several fleets of brightly colored bikes appeared on the streets. Under regulations established by DDOT for the dockless bikeshare pilot program, each operator is permitted to have a maximum of 400 vehicles on the street at any given time. For the first several months of the pilot program, vehicle was synonymous with bike until electric scooters were introduced and Lime reduced the number of bikes in their fleet in order to increase the number of scooters.  The pilot program presented a unique opportunity to study the effect that the introduction of a new mode of might have on the demand for a well-established bikeshare system. In this paper we use machine learning to predict the demand for CaBi through the duration of the pilot program, and by comparing the predicted demand with the actual demand, we attempt to determine to what extent the dockless bikeshare operators have been able to disrupt the status quo. 

## Data Sourcing and Architecture

![alt text](./readme_images/Data_Architecture_CaBiData.png "")

![alt text](./readme_images/Data_Architecture_DocklessData.png "")

![alt text](./readme_images/Data_Architecture_SecondaryData.png "")

![alt text](./readme_images/Data_Architecture_DataFlowDiagram2.png "")

## Capital Bikeshare Exploration

## Machine Learning

## Acknowledgements

