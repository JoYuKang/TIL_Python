
from collections import deque
import sys
sys.setrecursionlimit(10**6)

xLen, yLen = 0, 0
def solution(maps):
    global xLen, yLen
    xLen = len(maps)
    yLen = len(maps[0])
    answer = 0

    answer = bfs(0, 0, maps)


    return answer

def bfs(x, y, maps):
    global xLen, yLen
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= xLen or ny >= yLen:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[xLen - 1][yLen - 1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))