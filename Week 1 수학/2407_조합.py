
from math import factorial


n, m = map(int, input().split())

result = factorial(n) // (factorial(n-m) * factorial(m))
print(result)

