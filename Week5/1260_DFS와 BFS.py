
from collections import deque

import sys

N, M, V = map(int,sys.stdin.readline().strip().split())
graph = [ [] for x in range(N + 1)]
for i in range(M):
    a,b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()


visit = [0] * (N + 1)
count = 0

arrDfs = []
arrBfs = deque()
def dfs(V):
    if visit[V] == 0:
        visit[V] = 1
        arrDfs.append(V)
        for i in graph[V]:
            if visit[i] == 0:
                dfs(i)

dfs(V)
print(*arrDfs)

visit = [0] * (N + 1)
def bfs(V):
    queue = deque([V])
    visit[V] = 1
    while queue:
        now = queue.popleft()
        arrBfs.append(now)
        for i in graph[now]:
            if visit[i] == 0:
                visit[i] = 1
                queue.append(i)

bfs(V)

print(*arrBfs)


