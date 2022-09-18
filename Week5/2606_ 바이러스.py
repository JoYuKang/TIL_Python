
import readline
import sys


num = int(sys.stdin.readline().strip())
circle =  int(sys.stdin.readline().strip())
# graph= [[] * num]
graph= [[] for x in range(num + 1)]
for i in range(circle):
    a,b = map( int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0] * (num + 1)
def dfs(n):
    if visit[n] == 0:
        visit[n] = 1
        for i in graph[n]:
            dfs(i)
dfs(1)
result = -1
for i in visit:
    if i == 1:
        result += 1

print(result)
