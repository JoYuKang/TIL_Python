
from math import gcd


n, m = map(int, input().split())

arr = list(map(int,input().split()))

gcdArr = []

for i in arr:
    if m > i:
        gcdArr.append(m - i)
    elif m < i:
        gcdArr.append(i - m)

result = gcdArr[0]
for i in gcdArr:
    result = gcd(result, i)

print(result)
