# coding:utf-8
from sklearn import tree, neighbors
from sklearn.datasets import load_iris
import pandas as pd

# X = [[0, 0], [1, 1], [0.1, 0.2], [1.2, 1.2]]
# Y = [0, 1, 0, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(X, Y)
# print clf.predict([[0.1, 0.2], [0.8, 0.9]])
#

# iris = load_iris()
# # print iris
# data = iris.data
# target = iris.target
# clf = tree.DecisionTreeClassifier().fit(data, target)
# print clf.predict([[4.5, 3.8, 4.2, 5.8]])

# data = [[3, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 3, 0, 0]]
# target = [1, 2]
# clf = tree.DecisionTreeClassifier().fit(data, target)
# print clf.predict([[3, 2, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 2, 1, 0]])


# df = pd.read_excel('data.xlsx', index_col=None)
# # equal 0, notequal 1, normal 2
# data = df[2:].iloc[:, :12].values
# target = [0, 0, 0, 1, 1, 1, 2, 2, 2]
# # decisionTree
# clf = tree.DecisionTreeClassifier().fit(data, target)
# print clf.predict([[5, 2, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0], [1, 2, 0, 5, 1, 0, 0, 1, 0, 4, 1, 0]])

# # knn
# knn = neighbors.KNeighborsClassifier().fit(data, target)
# print knn.predict([[5, 2, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0], [1, 2, 0, 5, 1, 0, 0, 1, 0, 4, 1, 0]])

lst = [[5, 2, 0, 0, 0, 0, 0, 0, 0, 5, 1, 0], [1, 2, 0, 5, 1, 0, 0, 1, 0, 4, 1, 0]]

