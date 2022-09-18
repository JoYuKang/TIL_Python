
import sys


num = int(sys.stdin.readline().strip())

def dfs(n):
    global visit, arr
    if visit[n] == 0:
        visit[n] = 1
        dfs(arr[n])



for i in range(num):
    n = int(sys.stdin.readline().strip())
    visit = [0] * (n + 1)
    arr = [0] + list(map(int, sys.stdin.readline().strip().split()))
    count = 0
    # print(arr)
    for j in range(1, len(arr)):
        if visit[arr[j]] == 0:
            visit[j] = 1
            dfs(arr[j])
            count += 1
    print(count)
