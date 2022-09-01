
import sys


num = int(sys.stdin.readline().strip())
arr = []
for i in range(num):
    arr.append(int(sys.stdin.readline().strip()))

maxNum = int(max(arr))
result = [0, 1, 1, 1] 

for i in range(4, 101):
    result.append(result[i - 3] + result[i - 2])

for i in arr:
    print(result[i])


