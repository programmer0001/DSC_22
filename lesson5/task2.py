import numpy as np
import pandas as pd
import ML_mst as mst
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from lesson5.ML_KNN_manual import KNN_classifier, Scaler, train_test_split_df

cmap_bold = ListedColormap(['blue', '#FFFF00', 'black', 'green'])
np.random.seed = 2021
X_D2, y_D2 = make_blobs(n_samples=300, n_features=2, centers=8,
                        cluster_std=1.3, random_state=4)
y_D2 = y_D2 % 2

df = pd.DataFrame(X_D2, y_D2)
# shuffle dataframe
df = df.sample(frac=1)
# print general information about data
print(df.to_string())
# mst.print_df_info(df)

# split  df to train and test default value of percentage = 0,75
train_df, test_df = train_test_split_df(df, 0.9)
print('len(train_df)={:,}'.format(len(train_df)))
print('len(test_df)={:,}'.format(len(test_df)))

# select X (features) and y (labels)
X_train = train_df[[0, 1]]
y_train = train_df[[0, 1]]
X_test = test_df[[0, 1]]
y_test = test_df[[0, 1]]

print('X_train.shape=', X_train.shape)
print('y_train.shape=', y_train.shape)
print('X_test.shape=', X_test.shape)
print('y_test.shape=', y_test.shape)
print('X_train[0]= ', X_train.iloc[0])

# _dict = dict(zip(df.index.unique()))
# print(_dict)

scaler = Scaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# print(X_train_scaled)
print('X_train_scaled[0]= ', X_train_scaled.iloc[0])

n_neighbors = 5
clf = KNN_classifier(k_number=n_neighbors)
clf.fit(X_train_scaled, y_train)

print('score train = {:.3f}'.format(clf.score(X_train_scaled, y_train)))
print('score test = {:.3f}'.format(clf.score(X_test_scaled, y_test)))

k_best = None  # 'compute the best k'
score_best = None  # 'compute the best score'
print('The best k = {} , score = {}'.format(k_best, score_best))

# visualize decision boundary
