
from collections import deque


F, S, G, U, D = map(int, input().split())


def bfs(start, goal):
    queue = deque()
    visit = [0] * 1000001
    queue.append(start)
    visit[start] = 1
    while queue:
        next = queue.popleft()
        if next == goal:
            return visit[next] - 1
        for i in (next + U, next - D):
            if 0 < i <= F and visit[i] == 0:
                visit[i] = visit[next] + 1
                queue.append(i)
    return "use the stairs"

print(bfs(S ,G))
