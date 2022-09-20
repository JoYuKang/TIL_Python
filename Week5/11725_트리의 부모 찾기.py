import sys


sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())

graph = [[] for x in range(N + 1)]
visit = [0] * (N + 1)
for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    for i in graph[s]:
        if visit[i] == 0:
            visit[i] = s
            dfs(i)

dfs(1)        

print(*visit[2:], sep= "\n")