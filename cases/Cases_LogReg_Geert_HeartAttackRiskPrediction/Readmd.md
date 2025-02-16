# Heart Attack Risk Predicion

Notebook Logistic Regression Case
Oefening Data Scientist 
Geert Vandezande


Structure:\
cases/ \
├── Cases_HeartAttackRiskPrediction/ \
│ ├── data/ \
│ │ ├──  heart_attack_risk_dataset \
│ ├── Geert_HeartAttackRiskPrediction.ipynb│ ├── 
│ ├── README.md \
│ ├── images/ \
│ ├── logregcontinue.log


More info: see kaggle https://www.kaggle.com/datasets/arifmia/heart-attack-risk-dataset

pip install -f requirements.txt

Doel:
- Supervised Learning toepassen
- EDA uitvoeren op een dataset
- Logistic Regression toepassen op de data voor classificatie
- andere vormen van classificatie toepassen zonder en met hyper parameter tuning

Dataset: 
- More info: see kaggle https://www.kaggle.com/datasets/arifmia/heart-attack-risk-dataset


Volgorde van activiteiten in deze notebook: (cfr Datacamp "preparing data for modelling)
- data inlezen
- data bekijken, visueel en numerisch
- missing data oplossen 
- incorrect types controleren
- numerische waarde standardizeren
- categorische varaiabelen processen
- feature engineering
- select features for modelling
- eenvoudige logistic regression
- eenvoudige logistic regression en unbalance van de features corrigeren met SMOTE- en class_weight = 'unbalanced
- functie voor modeling met Logistic Regression, Decision Tree Regression en Random Forrest Regression, met uitvoering
- functie modeling met Hyperparameter tuning met GridSearchCV voor drie modellen, met uitvoering


Bij run ALL: (duurt 20 min)
- output in LogReg_continue.log
- de plots worden bewaard in de images\


Aantal testen werdern uitgevoerd, met en zonder SMOTE, met en zonder HyperParameter tuning maar de resultaten veranderen niet zo veel
Ook logistic regression met class_weight='balanced' maar op zich weinig verschil in de resultaten

De functies zijn geschreven. We kunnen nadien nog extra testen doen met bepaalde features wel of niet mee te nemen