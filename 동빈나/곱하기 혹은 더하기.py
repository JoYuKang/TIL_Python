
from unittest import result


num = input()

num = list(map(int, num))
result = 0
for i in num:
    if i < 2 or result < 2:
        result += i
    else:
        result *= i

print(result)

