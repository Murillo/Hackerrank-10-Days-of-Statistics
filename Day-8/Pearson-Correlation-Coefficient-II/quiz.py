"""
Pearson Correlation Coefficient II
Quiz: https://www.hackerrank.com/challenges/s10-mcq-7

regression X:
3x + 4y + 8 = 0
- 4y = 3x + 8
-y = 3x/4 + 8/4
-y = 3x/4 + 4 (reverse signal)
y = -3x/4 - 4
bx = -3/4

regression Y:
4x + 3y + 7 = 0
-4y = 3y + 7
-x = 3x/4 + 7/4 (reverse signal)
y =  -3x/4 - 7/4
by = -3/4

r² = bx * by
r² = -3/4 * -3/4
r² = 9/16
r +/- 3/4

if bx = by then
  r = -3/4
"""

print ("Result is: {}".format("-3/4"))
