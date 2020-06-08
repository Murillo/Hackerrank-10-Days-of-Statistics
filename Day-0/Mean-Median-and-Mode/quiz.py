import numpy as np
from scipy import stats

size = int(input())
numbers = [int(x) for x in raw_input().split()]
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
