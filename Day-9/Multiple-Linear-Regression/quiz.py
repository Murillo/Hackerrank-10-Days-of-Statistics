# Multiple Linear Regression
# Reference: https://www.hackerrank.com/challenges/s10-multiple-linear-regression/tutorial

# Question: https://www.hackerrank.com/challenges/s10-multiple-linear-regression

from sklearn import linear_model
x = [[5, 7], [6, 6], [7, 4], [8, 5], [9, 6]]
y = [10, 20, 60, 40, 50]
lm = linear_model.LinearRegression()
lm.fit(x, y)
a = lm.intercept_
b = lm.coef_
print ("{}, {}, {}".format(a, b[0], b[1]))
