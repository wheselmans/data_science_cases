Bron: case linear-regression van samarthpujari op Kaggle 
Notebook Optimization_Using_Gradient_Descent_in_Linear_Regression.ipynb moet uitgevoerd worden,
de notebook zal de data tvmarketing.csv (kolom marketing kosten en sales) uit dezelfde folder inlezen en lineaire regressie toepassen.
De regressie wordt met verschillende methoden opgesteld, nl. Numpy, SciKitLearn & Gradient Descent.

De testing/ controles zijn niet zelf uitgeschreven maar zijn functies uit file w2_unittest.py die opgeroepen worden.

Achterliggende functies w2_unittest.py:

-> test_load_data(target_adv)

Controleert of de ingevoerde dataset (target_adv) een Pandas DataFrame is.
Controleert de vorm van de dataset (200 rijen, 2 kolommen).
Vergelijkt enkele specifieke waarden van de kolommen "TV" en "Sales" met verwachte waarden.
Print testresultaten en fouten als de dataset niet aan de verwachtingen voldoet.


-> test_pred_numpy(target_pred_numpy)

Test een functie (target_pred_numpy(m, b, X)) die een lineaire regressievoorspelling maakt op basis van de formule:
𝑌=𝑚𝑋+𝑏
Vergelijkt de gegenereerde output met verwachte waarden.
Controleert of de uitvoer de juiste vorm heeft en numeriek correct is.

-> test_sklearn_fit(target_lr_sklearn)

Test of een LinearRegression model correct is getraind.
Controleert of het model de attributen coef_ en intercept_ bevat.
Vergelijkt de berekende coef_ (helling) en intercept_ met verwachte waarden.


->test_sklearn_predict(target_pred_sklearn, input_lr_sklearn)

Controleert of een sklearn-gebaseerde predictiefunctie (target_pred_sklearn(X, model)) de juiste voorspellingen maakt.
Vergelijkt de uitvoer met verwachte waarden.


->test_partial_derivatives(target_dEdm, target_dEdb, input_X_norm, input_Y_norm)

Test functies die de partiële afgeleiden van de foutfunctie berekenen ten opzichte van m en b (voor gradiëntdescent).
Controleert of de afgeleiden correct zijn voor specifieke invoerwaarden.


-> test_gradient_descent(target_gradient_descent, input_dEdm, input_dEdb, input_X_norm, input_Y_norm)

Test een gradiëntdescent-implementatie (target_gradient_descent) die m en b optimaliseert.
Controleert of de uiteindelijke waarden van m en b overeenkomen met verwachte waarden na een bepaald aantal iteraties.