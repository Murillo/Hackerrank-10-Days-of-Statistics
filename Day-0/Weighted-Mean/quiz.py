size = int(input())
numbers = list(map(float, input().strip().split(' ')))
weighted = list(map(float, input().strip().split(' ')))

sum_items = 0
for i in range(size):
    sum_items = sum_items + (numbers[i] * weighted[i])

print(round(sum_items/sum(weighted), 1))
