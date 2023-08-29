import pandas as pd
import joblib
import matplotlib.pyplot as plt



def preload_model():
    meanshift = joblib.load('./models/meanshift.pkl')
    return meanshift

def main():
    dataset = pd.read_csv('./data/candy.csv')

    x = dataset.drop('competitorname', axis=1)
    meanshift = preload_model()
    # r graficamente estos algoritmos de clustering
    plt.scatter(meanshift.cluster_centers_[:, 0], meanshift.cluster_centers_[:, 1], c='black', s=200)
    plt.show()

    

if __name__ == "__main__":
    main()