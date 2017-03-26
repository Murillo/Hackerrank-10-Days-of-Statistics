# Question: The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the
# first 5 inspections?

# Set data
probability = list(map(int, input().split()))
p = probability[0] / probability[1]
q = 1 - p
n = int(input())

# Get Geometric Distribution
result = 0
for i in range(n + 1):
    if i > 0:
        result = result + (q ** (i - 1) * p)

# Show the final result
print(round(result, 3))
