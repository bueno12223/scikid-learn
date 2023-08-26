import sklearn
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt
import pandas as pd

def main():

    dataset = pd.read_csv('./data/whr2017.csv')

    x = dataset[['gdp', 'family', 'lifexp', 'freedom', 'corruption', 'generosity', 'dystopia']]
    y = dataset[['score']]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    modelLineal = LinearRegression().fit(x_train, y_train)
    y_prediction = modelLineal.predict(x_test)

    modelLasso = Lasso(alpha=0.002).fit(x_train, y_train)
    y_prediction_lasso = modelLasso.predict(x_test)

    modelRigde = Ridge(alpha=1).fit(x_train, y_train)
    y_prediction_ridge = modelRigde.predict(x_test)

    linear_loss = mean_squared_error(y_test, y_prediction)
    print('Lineal loss', linear_loss)

    lasso_loss = mean_squared_error(y_test, y_prediction_lasso)
    print('Lasoo loss', lasso_loss)

    ridge_loss = mean_squared_error(y_test, y_prediction_ridge)
    print('Ridge loss', ridge_loss)

    print('='*32)

    print('Coef Lasso', modelLasso.coef_)
    print('Ridge Lasso', modelRigde.coef_)



if __name__ == '__main__':
    main()