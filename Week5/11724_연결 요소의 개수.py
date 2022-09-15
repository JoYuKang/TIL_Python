
import sys


N, M = map(int, sys.stdin.readline().strip().split())

graph = [ [] for x in range(N + 1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0] * (N + 1)

def dfs(num):
    if visit[num] == 0:
        visit[num] = 1
        for i in graph[num]:
            dfs(i)

count = 0
for i in range(1, N + 1):
    if visit[i] == 0:
        dfs(i)
        count += 1
print(count)

