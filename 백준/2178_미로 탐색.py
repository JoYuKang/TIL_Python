
from collections import deque

import sys


n, m = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

def bfs(x, y):
    queue.append((x,y))
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < m:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1

    return graph[n -1][m - 1] 

print(bfs(0, 0))



