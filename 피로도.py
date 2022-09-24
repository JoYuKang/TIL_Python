visit = []
answer = 0
def solution(k, dungeons):
    global visit
    visit = [0] * len(dungeons)
    
    dfs(k, 0, dungeons)

    
    return answer

def dfs(k, cnt, dungeons):
    global answer, visit
    if cnt > answer:
        answer = cnt

    for j in range(len(dungeons)):
        if k >= dungeons[j][0] and not visit[j]:
            visit[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visit[j] = 0


print(solution(80,[[80,20],[50,40],[30,10]]))