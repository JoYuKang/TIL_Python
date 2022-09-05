

from random import randrange
import sys


num = int(sys.stdin.readline().strip())
arr = []

for i in range(num):
    arr.append(int(sys.stdin.readline().strip()))

maxnum = max(arr)

result = [0, 1, 2, 4] + [0] * (maxnum - 3)

for i in range(4, maxnum + 1):
    result[i] = result[i - 1] + result[i - 2] + result[i - 3]

for i in range(num):
    print(result[arr[i]])




