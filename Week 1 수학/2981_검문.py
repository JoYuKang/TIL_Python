
from math import gcd, sqrt
import sys


n = int(sys.stdin.readline().strip())

arr = []
gcdArr = []
result = []

for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

arr = sorted(arr)

for i in range(0, len(arr) - 1):
    gcdArr.append(arr[i + 1] - arr[i])

gcdArr = sorted(gcdArr)

num = gcdArr[0]
for i in range(0, len(gcdArr) - 1):
    num = gcd(gcdArr[i + 1], num)


for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        result.append(i)
        if i != num // i:
            result.append(num // i)
result.append(num)
result = list(set(result))
result = sorted(result)

print(' '.join(map(str, result)))