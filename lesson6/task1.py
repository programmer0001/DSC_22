import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston
X, y = load_boston(return_X_y=True)
df = pd.DataFrame(X, columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX',
                              'RM', 'AGE', 'DIS', 'RAD', 'TAX',
                              'PTRATIO', 'B', 'LSTAT'])

df = df[['RM']]  # Note: returns df comparing to  df['RM']
df['target'] = y
print(df.head(10))
df.describe()

df.plot.scatter('RM', 'target')

X, y = load_boston(return_X_y=True)

# YOUR_CODE. select the values of feature 5 only (corresponding to 'RM') and assign to X
# START_CODE
X = None
# END_CODE

X = X.reshape(-1, 1)  # make it 2d as for case of mutivariable

# YOUR_CODE. Apply train_test_split to X and Y to get X_train, X_test, y_train, y_test
# START_CODE
X_train, X_test, y_train, y_test = None, None, None, None
# END_CODE

# DON'T_CHANGE_THIS_CODE. It is used to let you check the result is correct
print('X_train.shape= ', X_train.shape)
print('y_train.shape= ', y_train.shape)
X_train[:10]


class Linear_Regression_1():
    def __init__(self):
        pass

    def h(self, b, w, X):
        '''
        :param b -  float or ndarry of shape [m,1], m - number of samples
        :param w - ndarray of shape [1,m],  n - number of features
        :param X - ndarray of shape [m,n], m - number of samples, n - number of features
        '''
        assert (X.shape[1] == w.shape[1])

        # YOUR_CODE. Assign expression for h to h_res
        # START_CODE
        h_res = None
        # END_CODE

        return h_res

# DON'T_CHANGE_THIS_CODE. It is used to let you check the result is correct
np.random.seed(2018)
b_check= np.random.randn()
w_check= np.random.randn(1,1)
X_check= np.random.randn(10,1)
print('b= {}, \nw= {}, \nX= \n{}'.format(b_check, w_check, X_check))
lin_reg_1 = Linear_Regression_1()
lin_reg_1.h(b_check, w_check, X_check)


class Linear_Regression_2():
    '''linear regression using gradient descent
    '''

    def __init__(self):
        pass

    def J(self, h, y):
        '''
        :param h - ndarray of shape (m,1)
        :param y - ndarray of shape (m,1)
        :return expression for cost function
        '''
        if h.shape != y.shape:
            print('h.shape = {} does not match y.shape = {}.Expected {}'.format(h.shape, y.shape, (self.m, 1)))
            raise Exception('Check assertion in J')

            # YOUR_CODE. Assign expression for J to J_res
        # START_CODE
        J_res = None
        # END_CODE
        return J_res