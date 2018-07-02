# coding:utf-8
from sklearn import linear_model
import seaborn as sns


clf = linear_model.LinearRegression()

# [0, 0], [1, 1], [2, 2], [3, 3], [6, 6]
train = [[0], [1], [2.1], [3.5], [6]]
target = [0, 1, 2.2, 3.2, 6.6]

clf.fit(train, target)
print clf.predict([[2], [8], [10]])
