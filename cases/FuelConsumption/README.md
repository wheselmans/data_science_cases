FuelConsumption_Lineaire_Regressie

Created by Herman Steurs

Structure:
cases/
├── FuelConsumption/
│ ├── data/
│ │ ├── FuelConsumption_dataset
│ ├── FuelConsumption_Lineaire_Regressie.ipynb
│ ├── Sweetviz_FuelConsumption.html
│ ├── Kaggle_notebook.ipynb
│ ├── requirements.txt
│ ├── README.md \

More info see kaggle:
https://www.kaggle.com/datasets/krupadharamshi/fuelconsumption
https://www.kaggle.com/code/dogukantabak/7-regression-models-max-98-57/input


# Over de file
De dataset "Fuelconsumption" bevat informatie over verschillende voertuigen die in het jaar 2000 zijn geproduceerd. Het omvat details zoals het merk, model, voertuigklasse, motorinhoud, aantal cilinders, transmissietype en brandstoftype. Daarnaast biedt de dataset reeksen voor brandstofverbruik en CO2-uitstoot, wat inzicht geeft in de milieu-impact van elk voertuig.

De dataset bestrijkt een breed scala aan voertuigtypen, van compacte auto's tot middelgrote modellen, en bevat zowel conventionele als high-performance voertuigen. Met deze informatie kunnen analisten en onderzoekers trends bestuderen op het gebied van voertuigkenmerken, brandstofefficiëntie en emissies.

# Kolommen
YEAR: jaar van productie van de wagen
MAKE: merk van de wagen
MODEL: model
VEHICLE CLASS: klasse van de wagen: compact, mid-size, subcompact, etc.
ENGINE SIZE: inhoud van de motor
CYLINDERS: aantal cylinders
TRANSMISSION: versnellingsbak: automaat (A4, AS5) of manueel (M5, M6).
FUEL: type van de brandstof
FUEL CONSUMPTION: verbruik
COEMISSIONS: CO² uitstoot 

# Bevindingen
De Kaggle bereikt een modelscore van 98,57%.  (model.score(X_test, y_test))

Na het toepassen van de volgende technieken is het resultaat niet verbetert waarschijnlijk omdat de data set te klein was en de Kaggle persoon geen duplicates heeft verwijderd.

LabelEncoder, omzetten van de categorische kolommen naar numerische nadat ik een duplicate heb verwijderd. score 97,56%
box-cox transformatie, wegwerken van de skewness op de target kolom. score 97,03%
StandardScaler toepassen op de features. score 97,03% 
RobustScaler toepassen op de features. score 97,03%
Feature engineering, features verwijderen. score 96,85%
Feature engineering, features samenvoegen. score 96,58%
Lasso score 96,43% 
Ridge score 96,43%
Verwijderen outliers score 97,18%