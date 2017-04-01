# Confidence interval

# Question: You have a sample of 100 values from a population with mean u = 500
# and with standard deviation a = 80. Compute the interval that covers the
# middle 95% of the distribution of the sample mean; in other words, compute
# A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note
# that z is the z-score.

# Import library
import math

# Set data
n = float(input())
mean = float(input())
std = float(input())
percent_ci = float(input())
value_ci = float(input())

# Formula CI
ci = value_ci * (std / math.sqrt(n))

# Gets the result and show on the screen
print(round(mean - ci, 2))
print(round(mean + ci, 2))
