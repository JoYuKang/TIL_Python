import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 상,하,좌,우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if (0 <= nx < n) and (0 <= ny < m):
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1
                dfs(nx, ny)

t = int(sys.stdin.readline().strip())

for count in range(t):
    m, n, k = map(int,sys.stdin.readline().strip().split())

    graph = [[0 for j in range(m)] for i in range(n)]
    count = 0
    for i in range(k):
        a, b = map(int,sys.stdin.readline().strip().split())
        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dfs(i, j)
                count += 1
    print(count)


