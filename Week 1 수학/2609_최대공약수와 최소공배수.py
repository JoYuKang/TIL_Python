
from math import gcd


n,m = map(int,input().split())


gcdNum = gcd(n,m)
print(gcdNum)

print(int(n * m / gcdNum))

