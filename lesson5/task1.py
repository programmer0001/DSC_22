from ML_KNN_manual import train_test_split_df
from ML_KNN_manual import KNN_classifier
from sklearn.datasets import load_iris
from ML_KNN_manual import Scaler
# import matplotlib.pyplot as plt
import ML_mst as mst
import pandas as pd
import numpy as np


np.random.seed = 2021
iris = load_iris()
print('data contains:', iris.keys())
X, y = iris.data, iris.target
labels, feature_names = iris.target_names, iris['feature_names']
df_iris = pd.DataFrame(X, columns=feature_names)
df_iris['label'] = y
features_dict = {k: v for k, v in enumerate(labels)}
df_iris['label_names'] = df_iris.label.apply(lambda x: features_dict[x])

mst.print_df_info(df_iris, column_values_count='label_names')
df_iris = df_iris.sample(frac=1)
mst.print_df_info(df_iris, column_values_count='label_names')

train_df, test_df = train_test_split_df(df_iris, 0.9)
# print(train_df.columns)
print('len(train_df)={:,}'.format(len(train_df)))
print('len(test_df)={:,}'.format(len(test_df)))

X_train = train_df[['sepal length (cm)', 'sepal width (cm)']]
                   # 'petal length (cm)', 'petal width (cm)']]
y_train = train_df['label']
X_test = test_df[['sepal length (cm)', 'sepal width (cm)']]
                  # 'petal length (cm)', 'petal width (cm)']]
y_test = test_df['label']

print('X_train.shape=', X_train.shape)
print('y_train.shape=', y_train.shape)
print('X_test.shape=', X_test.shape)
print('y_test.shape=', y_test.shape)
print('X_train[0]=', X_train.iloc[0])

flower_dict = dict(zip(df_iris['label'].unique(),
                       df_iris['label_names'].unique()))
print(flower_dict)

scaler = Scaler()
X_train_scaled = scaler.fit_transform(X_train)
print(X_train_scaled)
X_test_scaled = scaler.transform(X_test)
print('X_train_scaled[0]=\n', X_train_scaled.iloc[0])

n_neighbors = 5
clf = KNN_classifier(k_number=n_neighbors)
clf.fit(X_test_scaled, y_train)

print('score train = {:.3f}'.format(clf.score(X_train_scaled, y_train)))
print('score test = {:.3f}'.format(clf.score(X_test_scaled, y_test)))

target_observation = pd.Series({'sepal length (cm)': 5.0,
                                'sepal width (cm)': 3.0,
                                'petal length (cm)': 2.0,
                                'petal width (cm)': 0.81})
print(target_observation)
target_observation_scaled = scaler.transform(target_observation)
print('target_observation_scaled=')
print(target_observation_scaled)

target_observation_label_predicted = clf.predict(target_observation_scaled)
print('for {} \n\npredicted fruit name = {} [label = {}] '.
      format(dict(target_observation_scaled),
             flower_dict[target_observation_label_predicted],
             target_observation_label_predicted))

k_best = None  # 'compute the best k'
score_best = None  # 'compute the best score'

print('The best k = {} , score = {}'.format(k_best, score_best))
