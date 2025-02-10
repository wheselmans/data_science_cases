Bron: logistic-regression-implementation van kanncaa1 op Kaggle

Voer de notebook logistic-regression-implementation.ipynb uit.
Deze haalt data uit input\data.csv, dewelke de "Breast Cancer Wisconsin (Diagnostic) Data Set".
Kolom diagnosis bevat "The diagnosis of breast tissues (M = malignant, B = benign)", dewelke te voorspellen is.

stappen notebook:
-> data inlezen
-> "manuele" normalisatie van X
-> train/test split
-> functies 
        weights & biases
        sigmoid (y waarde tussen 0 en 1)
        forward & back propagation
        update learning parameters
        predict
        logistic regression
-> uitvoeren logistic regression + estimatie kosten + train/test accuracy zelf opgezet (+- 94%)
-> train/ test accuracy met sklearn logaritmische regressie (+- 97%)