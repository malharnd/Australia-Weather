# Rainfall-prediction-in-Australia
_________________________________________________________________________________________________________________________________________________________________________________

## Rain in Australia
### Description
This dataset contains daily weather observations from numerous Australian weather stations.

_________________________________________________________________________________________________________________________________________________________________________________


### Features description
Date---The date of observation

Location---The common name of the location of the weather station

MinTemp---The minimum temperature in degrees celsius

MaxTemp---The maximum temperature in degrees celsius

Rainfall---The amount of rainfall recorded for the day in mm

Evaporation---The so-called Class A pan evaporation (mm) in the 24 hours to 9am

Sunshine---The number of hours of bright sunshine in the day.

WindGustDir---The direction of the strongest wind gust in the 24 hours to midnight

WindGustSpeed---The speed (km/h) of the strongest wind gust in the 24 hours to midnight

MeanHumidity---Humidity (percent) at 9am and 3pm

MeanPressure---Atmospheric pressure (hpa) reduced mean sea level at 9am and 3pm

MeanTemp9---Temperature (degrees C) at 9am and 3pm

RainToday---Boolean: 1 if precipitation (mm) in the 24 hours to 9am exceeds 1mm, otherwise 0

RainTomorrow---The target variable. Did it rain tomorrow?

References
This total dataset is taken from following kaggle reference.

https://www.kaggle.com/jsphyg/weather-dataset-rattle-package

### Source & Acknowledgements
Observations were drawn from numerous weather stations. The daily observations are available from http://www.bom.gov.au/climate/data. Copyright Commonwealth of Australia 2010, Bureau of Meteorology.


### Objective
Predict whether or not it will rain tomorrow by training a binary classification model on target RainTomorrow.

The target variable RainTomorrow means: Did it rain the next day? Yes or No.

_________________________________________________________________________________________________________________________________________________________________________________

1.Scatter Plot 

This scatter plot shows the relationship of rain tomorrow on minTemp and maxTemp of the previous.
 
<img width="500" alt="Screenshot 2022-12-03 at 12 56 25 AM" src="https://user-images.githubusercontent.com/64124824/205371068-ad9d0cf3-ec66-4744-aa88-02e14146de87.png">


This scatter plot shows the relationship of rain tomorrow on Mean_Humidity and Mean_temp of the previous.

<img width="500" alt="Screenshot 2022-12-03 at 12 56 40 AM" src="https://user-images.githubusercontent.com/64124824/205371148-d99fcd0d-9529-4215-8483-3293bba30504.png">


 
This scatter plot shows the relationship of rain tomorrow on minTemp and MeanHumidty of the previous.

<img width="500" alt="Screenshot 2022-12-03 at 12 56 52 AM" src="https://user-images.githubusercontent.com/64124824/205371189-ccd4e4ab-0f79-4e90-95c9-14af8060f320.png">

2.Heapmap
 
This heatmap shows the correlation between all features.

<img width="500" alt="Screenshot 2022-12-03 at 12 57 10 AM" src="https://user-images.githubusercontent.com/64124824/205371226-c03f2355-857d-43ec-b67d-88e9c71b9298.png">

 
_________________________________________________________________________________________________________________________________________________________________________________
 
