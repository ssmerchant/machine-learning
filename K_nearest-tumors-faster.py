import numpy as np
from sklearn import model_selection, neighbors
import pandas as pd

accuracies = []

for i in range(25):
    df = pd.read_csv('breast-cancer-wisconsin-data.data')
    #replace missing data & drop ID column
    df.replace('?', -99999, inplace=True)
    df.drop(['id'], 1, inplace=True)

    X = np.array(df.drop(['class'], 1))
    y = np.array(df['class'])

    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size = 0.9)
    clf = neighbors.KNeighborsClassifier(n_jobs=-1)
    clf.fit(X_train, y_train)

    accuracy = clf.score(X_test, y_test)

    '''
    print(accuracy)

    #Example input to get prediction
    example_measures = np.array([[4, 2, 1, 1, 1, 2, 3, 2, 1], [10, 2, 1, 2, 2, 2, 3, 2, 1]])
    example_measures = example_measures.reshape(len(example_measures), -1)

    prediction = clf.predict(example_measures)
    print(prediction)
    '''

    accuracies.append(accuracy)

print(sum(accuracies) / len(accuracies))