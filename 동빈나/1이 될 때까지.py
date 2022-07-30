

from unittest import result


n,k =map(int, input().split())

result = 0
while True:
    target = (n // k) * k
    result += n - target
    if k > n:
        break
    n //= k
    result += 1

result += n - 1
print(result)