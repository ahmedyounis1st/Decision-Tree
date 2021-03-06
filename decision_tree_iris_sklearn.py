# -*- coding: utf-8 -*-
"""decision_tree_iris_sklearn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zFrP_JofsoqJx2kD4dM5hzF_t4s1usOb
"""

from sklearn.datasets import load_iris # import iris data set from sklearn library
from sklearn.tree import  DecisionTreeClassifier   
from sklearn.metrics import accuracy_score ,confusion_matrix

iris=load_iris()
X = iris.data
y = iris.target

iris.feature_names

iris.target_names

from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test= train_test_split(X, y,test_size=0.4, random_state =33)   
# X_train, X_test, y_train, y_test= train_test_split( X, y, test_size = 0.25, random_state = 41)

DTC=DecisionTreeClassifier(max_depth=3)
# DTC=DecisionTreeClassifier(max_depth=4)
DTC.fit(X_train,y_train)

DTC.classes_

y_pred=DTC.predict(X_test)

accuracy = accuracy_score(y_pred, y_test)
accuracy

print(confusion_matrix(y_test, y_pred))