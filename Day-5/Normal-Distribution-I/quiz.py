# Question: In a certain plant, the time taken to assemble a car is a random
# variable, X, having a normal distribution with a mean of 20 hours and a
# standard deviation of 2 hours. What is the probability that a car can be
# assembled at this plant in:
# 1. Less than 19.5 hours?
# 2. Between 20 and 22 hours?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
initial_values = list(map(float, input().split()))
mean = initial_values[0]
std = initial_values[1]
less_period = float(input())
between_period = list(map(float, input().split()))

# Gets the result and show on the screen
print (round(cumulative(mean, std, less_period),3))
print (round(cumulative(mean, std, between_period[1]) - cumulative(mean, std, between_period[0]), 3))
