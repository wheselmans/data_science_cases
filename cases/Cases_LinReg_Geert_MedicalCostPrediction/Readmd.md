# Insurance medical cost prediction

Created by Geert Vandezande, 20250217


Structure:\
cases/ \
├── Cases_LinReg_Geert_MedicalCostPrediction \
│ ├── data/ \
│ │ ├──  insurance.csv \
│ ├── CaseLinReg_MedicalCostPrediction.ipynb
│ ├── README.md \


More info: see kaggle
- https://www.kaggle.com/datasets/mirichoi0218/insurance/data


Some notebooks:
- https://www.kaggle.com/code/terrycycheng/medical-insurance-cost-eda-prediction
- https://www.kaggle.com/code/shitalandhalkar/regression-medical-cost-personal
- https://www.kaggle.com/code/terrycycheng/medical-insurance-cost-eda-prediction


pip install -f requirements.txt


Zie voor meer info in de eerste sectie van de notebook

Zie LinReg_continue.log voor info van de diverse testen

Zie alle_results.txt voor de resultaten van de diverse testen

Zie images\*. voor diverse plots van de variabelen


Conclusie:

Stratify op de charges levert betere resultaten op
Hyper parameter tuning levert nog lichte verbetering op

Maar vooral de opdeling van de dataset in rokers en niet-rokers resulteert is een veel beter model voor de rokers. Voor de niet-rokers is er geen verbetering. Hier kan nog verder onderzoek naar verricht worden




