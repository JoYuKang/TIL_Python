

import sys


arr = list(sys.stdin.readline().strip())
stack = []
sign = True
sum = 0
for i in arr:
    if i == "(":
        stack.append(i)
        sign = True
    else:
        stack.pop()
        if sign:
            sum += len(stack)
            sign = False
        else:
            sum += 1
print(sum)
        


