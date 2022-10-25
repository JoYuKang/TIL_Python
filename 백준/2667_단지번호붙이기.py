
from collections import deque
import sys


num = int(sys.stdin.readline().strip())

graph = [list(map(int, sys.stdin.readline().strip()))for _ in range(num)]

result = []
visit = [[0] * num for _ in range(num)]


def bfs(x, y):
    count = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visit[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < num and 0 <= ny < num:
                if visit[nx][ny] == 0 and graph[nx][ny] == 1:
                    count += 1
                    visit[nx][ny] = 1
                    queue.append((nx, ny))
    return count

for i in range(num):
    for j in range(num):
        if graph[i][j] == 1 and visit[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])