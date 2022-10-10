def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    for com in range(n):
        if visited[com] == 0:
            DFS(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer

def DFS(n, computers, com, visited):
    visited[com] = 1
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if visited[connect] == 0:
                DFS(n, computers, connect, visited)

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]	))