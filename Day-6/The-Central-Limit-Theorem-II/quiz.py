# Question: The number of tickets purchased by each student for the
# University X vs. University Y football game follows a distribution that has
# a mean of u = 2.4 and a standard deviation of 20.
# A few hours before the game starts, 100 eager students line up to purchase
# last-minute tickets. If there are only 250 tickets left, what is the
# probability that all 100 students will be able to purchase tickets?

# Import library
import math

# Define functions
def cumulative(mean, std, value):
    return 0.5 * (1 + math.erf((value - mean) / (std * (2 ** 0.5))))

# Set data
max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean = mean * n
new_std = math.sqrt(n) * std

# Gets the result and show on the screen
print (round(cumulative(new_mean, new_std, max_weight),4))
