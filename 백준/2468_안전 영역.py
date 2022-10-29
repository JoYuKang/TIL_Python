
from collections import deque
import sys
sys.setrecursionlimit(10000)

num = int(sys.stdin.readline().strip())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(num)]

graphLen = num

def bfs(x, y, num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= graphLen or ny < 0 or ny >= graphLen: continue
            if visit[nx][ny] > 0 or graph[nx][ny] <= num: continue
            visit[nx][ny] = 1
            queue.append((nx, ny))

result = 0
for num in range(0, 101):
    visit = [[0] * graphLen for _ in range(graphLen)]
    maxNum = 0
    for i in range(graphLen):
        for j in range(graphLen):
            if graph[i][j] > num and visit[i][j] == 0:
                bfs(i, j, num)
                maxNum += 1
    result = max(result, maxNum)

print(result)
