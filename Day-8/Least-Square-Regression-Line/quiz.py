# Linear Regression
# Reference: https://en.wikipedia.org/wiki/Linear_regression

# Question: https://www.hackerrank.com/challenges/s10-least-square-regression-line

# import library
import statistics as st

# Set data
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]
mean_x = st.mean(x)
mean_y = st.mean(y)
x_squared = sum([x[i] ** 2 for i in range(5)])
xy = sum([x[i]*y[i] for i in range(5)])

# Set the B and A
b = (n * xy - sum(x) * sum(y)) / (n * x_squared - (sum(x) ** 2))
a = mean_y - b * mean_x

# Gets the result and show on the screen
print (round(a + 80 * b, 3))
