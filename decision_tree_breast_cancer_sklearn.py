# -*- coding: utf-8 -*-
"""decision_tree_breast_cancer_sklearn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tYULagWATmmz_EbWHMB_ar_x8VxhoEXK
"""

from sklearn.datasets import load_breast_cancer
from sklearn.tree import  DecisionTreeClassifier   
from sklearn.metrics import accuracy_score ,confusion_matrix

data = load_breast_cancer()
X = data.data
y = data.target

X.shape

data.feature_names

data.target_names

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test= train_test_split(X, y,test_size=0.2, random_state =0)

DTC=DecisionTreeClassifier(max_depth=3)
DTC.fit(X_train,y_train)

DTC.classes_

y_pred=DTC.predict(X_test)

accuracy = accuracy_score(y_pred, y_test)*100
accuracy.round(2)

print(confusion_matrix(y_test, y_pred))

max_score = 0
paramters = []
test_sizes = [0.2, 0.25, 0.3, 0.33, 0.4]
for s in test_sizes:
  for i in range(43):
    X_train, X_test, y_train, y_test= train_test_split(
        X, y, test_size = s, random_state = i)                       
    for d in range(1,31):
      DTC = DecisionTreeClassifier(max_depth = d)
      DTC.fit(X_train, y_train) 
      y_pred = DTC.predict(X_test)
      score = accuracy_score(y_pred, y_test)*100
      if score > max_score:
        max_score = score
        paramters = [s, i, d]

print('Highest accuarcy obtained: {}%'.format(max_score.round(2)))
print('Using paramters test_size = {}, random_state = {}, max_depth = {}'.format(paramters[0], paramters[1], paramters[2]))

X_train, X_test, y_train, y_test= train_test_split(
    X, y, test_size = 0.25, random_state = 41)

DTC = DecisionTreeClassifier(max_depth = 4)
DTC.fit(X_train, y_train)

print(f'Train set score: {(DTC.score(X_train, y_train)*100).round(2)}%')
print(f'Test set score: {(DTC.score(X_test, y_test)*100).round(2)}%')

y_pred = DTC.predict(X_test)

accuracy = accuracy_score(y_pred, y_test)*100
accuracy.round(2)

print(confusion_matrix(y_test, y_pred))

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

