def solution(n, computers):
    visited = [False] * n
    answer = 0

    def dfs(pc):
        visited[pc] = True
        for idx, c in enumerate(computers[pc]):  #
            if c and not visited[idx]:
                dfs(idx)

    for pc in range(n):
        if not visited[pc]:
            dfs(pc)
            answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))