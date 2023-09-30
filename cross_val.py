import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_val_score, KFold

def main():
    dt = pd.read_csv('./data/felicidad_corrupt.csv')

    x = dt.drop(['country', 'score'], axis=1)
    y = dt['score']

    model = DecisionTreeRegressor()
    score = cross_val_score(model, x, y, cv=3, scoring='neg_mean_squared_error')

    print(np.abs(np.mean(score)))

    kf = KFold(n_splits=3, shuffle=True, random_state=42)

    validations_scores = []

    for train, test in kf.split(dt):
        model.fit(x.iloc[train], y.iloc[train])
        score = model.score(x.iloc[test], y.iloc[test])
        validations_scores.append(score)

    print(np.abs(np.mean(validations_scores)))





if __name__ == '__main__':
    main()