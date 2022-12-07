from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=4)

k_range = range(1, 26)
scores = {}
scores_list = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_predict = knn.predict(X_test)
    scores[k] = metrics.accuracy_score(y_test, y_predict)
    scores_list.append(metrics.accuracy_score(y_test, y_predict))

print("Features = {}. Label = {}.".format(X_test[0], knn.predict([X_test[0]])))
# print(y_predict)
# Show results
print("Scores: ")
for i in scores:
    print(i, ' - ', scores[i])
the_best_neighbours = max(scores, key=scores.get)
print("The best score with {} neighbors. Score = {}".format(the_best_neighbours,
                                                            scores[the_best_neighbours]))
