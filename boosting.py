import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
   dt_heart = pd.read_csv('./data/heart.csv')

   x = dt_heart.drop(['target'], axis=1)
   y = dt_heart['target']

   dt_train, td_test, t_train, t_test = train_test_split(x, y, test_size=0.35)

   knn_class = KNeighborsClassifier().fit(dt_train, t_train)
   t_predict_knn = knn_class.predict(td_test)
   print(accuracy_score(t_predict_knn, t_test))

   boost = GradientBoostingClassifier(loss='exponential',learning_rate=0.15, n_estimators=100, max_depth=5).fit(dt_train, t_train)
   t_predict_boost = boost.predict(td_test)
   print(accuracy_score(t_predict_boost, t_test))

if __name__ == "__main__":
    main()