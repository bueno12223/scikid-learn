import pandas as pd

from sklearn.linear_model import RANSACRegressor, HuberRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def main():
    data = pd.read_csv('./data/felicidad_corrupt.csv')
    x = data.drop(['country', 'score'], axis=1)
    y = data[['score']]

    dt_train, dt_test, t_train, t_test = train_test_split(x, y, train_size=0.3, random_state=42)

    estimators = {
        'SVR': SVR(gamma='auto', C=1.0, epsilon=0.1),
        'RANSAC': RANSACRegressor(),
        'HUBER': HuberRegressor(epsilon=1.35)
    }

    for name, estimator in estimators.items():
        estimator.fit(dt_train, t_train)
        t_prediction = estimator.predict(dt_test)

        error_loss = mean_squared_error(t_test, t_prediction)
        print(f'The {name} models predicts: {error_loss}')
        print('='*64)


if __name__ == "__main__":
    main()