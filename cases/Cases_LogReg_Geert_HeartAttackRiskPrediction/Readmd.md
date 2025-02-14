# Heart Attack Risk Predicion

Notebook Logistic Regression Case
Oefening Data Scientist 
Geert Vandezande


Structure:\
cases/ \
├── HeartAttackRiskPrediction/ \
│ ├── data/ \
│ │ ├──  heart_attack_risk_dataset \
│ ├── CaseLogReg_HeartAttackRickPrediction.ipynb│ ├── 
│ ├── README.md \
│ ├── images/ \



More info: see kaggle https://www.kaggle.com/datasets/arifmia/heart-attack-risk-dataset


pip install -f requirements.txt



Doel:
- Supervised Learning toepassen
- EDA uitvoeren op een dataset
- Logistic Regression toepassen op de data voor classificatie
- andere vormen van classificatie toepassen

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
- eenvoudige logistic regression en unbalance van de features corrigeren met SMOTE- 
- modeling met Logistic Regression, Decision Tree Regression en Random Forrest Regression
- modeling met Hyperparameter tuning met GridSearchCV voor model Random Forrest en DecisionTreeClassifier


Tijdens de uitvoering worden de plots gesaved naar images\ en wordt er een log file aangemaakt logreg_continue.log.
Deze wordt enkel verwijderd bij een run all. Indien nodig, verwijder deze zelf
