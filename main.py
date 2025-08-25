import pandas as pd

def generateCLASSIFIER():
    dataset = pd.read_csv("Data.xls.csv")
    dataset=dataset.dropna()
    X=dataset.iloc[:,1].values
    X=X.reshape(-1,1)
    y = dataset.iloc[:, 3].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    from sklearn.neighbors import KNeighborsClassifier

    Classifier=KNeighborsClassifier(n_neighbors=5)

    Classifier.fit(X_train, y_train)

    import pickle

    pickle.dump(Classifierlassifier,open('model.pkl','wb'))