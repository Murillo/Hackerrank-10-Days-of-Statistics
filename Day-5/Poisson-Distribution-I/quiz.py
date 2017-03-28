# Question: A random variable, X, follows Poisson distribution with mean of 2.5
# Find the probability with which the random variable X is equal to 5.

# Define functions
def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n > 1:
        return factorial(n - 1) * n

# Set data
mean = float(input())
k = float(input())
e = 2.71828

# Gets the result and show on the screen
result = ((mean ** k) * (e ** -mean)) /  factorial(k)
print(round(result, 3))
