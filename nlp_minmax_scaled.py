import pandas as pd
pd.options.display.max_columns=1000
pd.options.display.width=200
pd.options.display.min_rows=60
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn import preprocessing

from datetime import datetime


def compare_dicts(a, b,
                  ignore=['test_score', 'train_score', 'tn', 'fn', 'tp', 'fp', 'f1_score', 'precision', 'recall']):
    a = dict(a)
    b = dict(b)
    for k in ignore:
        a.pop(k, None)
        b.pop(k, None)

    return tuple(a.items()) == tuple(b.items())

hyperparam_table = []

filename = 'data_cleanednlp2.csv'
df3 = pd.read_csv(filename)

# select only columns with int or float data types
df3 = df3.select_dtypes(['number'])
# drop any columns with null values
df3.dropna(axis=1, inplace=True)
# remove the class series
var_class3 = df3.pop('CLASS')

scaler = preprocessing.MinMaxScaler()
scaled_df = scaler.fit_transform(df3)
scaled_df = pd.DataFrame(scaled_df, columns=df3.columns)

x_train, x_test, y_train, y_test = train_test_split(scaled_df, var_class3, test_size=0.05, random_state=0)
x_train.to_csv(filename[:-4] + '_scaledxtrain.csv', index=False)
x_test.to_csv(filename[:-4] + '_scaledxtest.csv', index=False)
y_train.to_csv(filename[:-4] + '_scaledytrain.csv', index=False, header=False)
y_test.to_csv(filename[:-4] + '_scaledytest.csv', index=False, header=False)

exists = any([compare_dicts(a, b={'test_size': 0.05,
                                  'random_state': 0,
                                  'data_size': str(df3.shape),
                                  'scaling': 'min_max',
                                  'filename': filename,
                                  'class_weight': 'balanced',
                                  'model': 'sklearn.LogisticRegression'
                                  })
              for a in hyperparam_table])

logisticRegr = LogisticRegression(class_weight='balanced')
if not exists:
    hyperparam_table += [{'test_size': 0.05,
                          'random_state': 0,
                          'data_size': str(df3.shape),
                          'scaling': 'min_max',
                          'filename': filename,
                          'class_weight': 'balanced',
                          'model': 'sklearn.LogisticRegression'
                          }]

    logisticRegr.fit(x_train, y_train)

    predictions_test = logisticRegr.predict(x_test)
    predictions_train = logisticRegr.predict(x_train)

    score = logisticRegr.score(x_test, y_test)
    hyperparam_table[-1]['test_score'] = score

    training_score = logisticRegr.score(x_train, y_train)
    hyperparam_table[-1]['train_score'] = training_score

    tn, fp, fn, tp = confusion_matrix(y_test, predictions_test).ravel()
    hyperparam_table[-1]['tn'] = tn
    hyperparam_table[-1]['fp'] = fp
    hyperparam_table[-1]['fn'] = fn
    hyperparam_table[-1]['tp'] = tp

    f1 = f1_score(y_test, predictions_test)
    hyperparam_table[-1]['f1_score'] = f1
    precision = precision_score(y_test, predictions_test)
    hyperparam_table[-1]['precision'] = precision
    recall = recall_score(y_test, predictions_test)
    hyperparam_table[-1]['recall'] = recall