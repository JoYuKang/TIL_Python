
from math import gcd


n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

totalA = 1
totalB = 1

for i in arr1:
    totalA *= i

for i in arr2:
    totalB *= i


strprint = str(gcd(totalA,totalB))

if len(strprint) > 9:
    print(strprint[-9:])
else:
    print(strprint)



