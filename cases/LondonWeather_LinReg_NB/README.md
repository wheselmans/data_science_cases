# data_science_cases
Predicting Temperature in London

## Dataset: 
 `london_weather.csv`contains the following columns:
- **date** - recorded date of measurement - (**int**)
- **cloud_cover** - cloud cover measurement in oktas - (**float**)
- **sunshine** - sunshine measurement in hours (hrs) - (**float**)
- **global_radiation** - irradiance measurement in Watt per square meter (W/m2) - (**float**)
- **max_temp** - maximum temperature recorded in degrees Celsius (°C) - (**float**)
- **mean_temp** - **target** mean temperature in degrees Celsius (°C) - (**float**)
- **min_temp** - minimum temperature recorded in degrees Celsius (°C) - (**float**)
- **precipitation** - precipitation measurement in millimeters (mm) - (**float**)
- **pressure** - pressure measurement in Pascals (Pa) - (**float**)
- **snow_depth** - snow depth measurement in centimeters (cm) - (**float**)

## Notebooks:
**0_original_project-predicting-temperature-in-london**
Author: Abdelaziz Sami
**1_running_original-predicting-temperature-in-london**
slightly addapted version: NB (read data from kaggle,recolored/-sized heatmap,replaced debricated features,... )
**2_TimeSeriesPrediction**
In this notebook the analysis is more focoused on time series. 

**Description(0 & 1):**
* Load & Inspect Data
* Process & Clean Data (change dtype of date to datetime, aggregation per month though later no longer used)
* Data Visualization (lineplot & correlation-heatmap)
* Feature Selection & Data Preparation
    * takes all features (dropping only temperature related features as predictors)
    * Drops missing values in the target variable (mean_temp)
    * Splits data without taking into account timeseries-characteristics
    * imputes missing values (mean) and scales the features
* Train & Evaluate Models (Linear Regression, Decision Tree, and Random Forest)
    * Iterates over different max_depth values for tree-based models.
    * Predicts on test data and calculates RMSE (Root Mean Squared Error).
    * Logs models and performance metrics using MLflow.

**Main disadvantage of the approach:**
- The predictions of temperature are done by features at the same time point. 
- None of the preprocessing steps takes into account time series modeling (train-test-split, prediction by lagged features, blocked cv)
- There is no controle for overfitting (which definitivly takes place with highdepth forest/tree models)

