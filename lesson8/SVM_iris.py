# YOUR_CODE.  Try linear, rbf and poly kernels
# START_CODE
from sklearn.svm import SVC
# from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target


def kernel_test(kernel, C, third):
    the_best = (0, 0)
    test_size = 0.15
    while test_size < 0.9:
        X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=test_size,
                                                        random_state=100)
        if kernel == 'linear':
            clf_svm = SVC(C=C, kernel=kernel, max_iter=third).fit(X_train1, y_train1)
        if kernel == 'rbf':
            clf_svm = SVC(C=C, kernel=kernel, gamma=third).fit(X_train1, y_train1)
        if kernel == 'poly':
            clf_svm = SVC(C=C, kernel=kernel, degree=third).fit(X_train1, y_train1)

        score_test = clf_svm.score(X_test1, y_test1)
        score_train = clf_svm.score(X_train1, y_train1)
        # print("size = {}. Score = {}, {}".format(round(test_size, 2), round(score_test, 4), round(score_train, 4)))
        if score_test > the_best[0]:
            the_best = (score_test, test_size)
        test_size += 0.01
    print("Kernel: ", kernel)
    print("The best test size is {}. Score = {} \n".format(round(the_best[1], 2), round(the_best[0], 4)))


kernel_test('linear', 1, 10000)
kernel_test('rbf', 10, 0.001)
kernel_test('poly', 5000, 3)
# END_CODE
