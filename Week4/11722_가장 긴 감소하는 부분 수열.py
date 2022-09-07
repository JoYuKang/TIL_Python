
import sys



num = int(sys.stdin.readline().strip())

arr = list(map(int, sys.stdin.readline().strip().split()))

dp = [1] * num

for i in range(1, num):
    for j in range(i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))

