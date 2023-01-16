from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.colors import ListedColormap
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn import metrics

cmap_bold = ListedColormap(['blue', '#FFFF00', 'black', 'green'])
X, y = make_blobs(n_samples=300, n_features=2, centers=8,
                  cluster_std=1.3, random_state=4)
y = y % 2

print(type(X))
print(type(y))
print(X[:10], '\n')
print(y[:10], '\n')
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

# Show results
the_best_neighbours = max(scores, key=scores.get)
print("Scores: ")
for i in scores:
    print(i, ' - ', scores[i])
print("The best score with {} neighbors. Score = {}".format(the_best_neighbours,
                                                            scores[the_best_neighbours]))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.scatter(X_train[:, 0], X_train[:, 1], c=y_train,
            marker='o', s=30, cmap=cmap_bold)
ax2.scatter(X_test[:, 0], X_test[:, 1], c=y_test,
            marker='o', s=30, cmap=cmap_bold)
plt.show()
