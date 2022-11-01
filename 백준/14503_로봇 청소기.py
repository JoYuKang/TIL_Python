
from collections import deque
import sys


n, m = map(int, sys.stdin.readline().strip().split())

r, c, d = map(int, sys.stdin.readline().strip().split())

graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

visit = [[0] * m for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit[r][c] = 1

answer = 1
while True:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4 
        nx = r + dx[d]
        ny = c + dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 1 or visit[nx][ny] == 1:
            continue
        visit[nx][ny] = 1
        answer += 1
        r = nx
        c = ny
        flag = 1
        break
    if flag == 0:
        if graph[r - dx[d]][c - dy[d]] == 1:
            print(answer)
            break
        else:
            r = r - dx[d]
            c = c - dy[d]
