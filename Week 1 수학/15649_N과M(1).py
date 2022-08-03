
N,M = map(int,input().split())

arr = []

visited = [False] * (N + 1)

def dfs():
    if len(arr) == M:
        print(' '.join(map(str,arr)))
    else:
        for i in range(1, N + 1):
            if visited[i] == False:
                arr.append(i)
                visited[i] = True
                dfs()
                arr.pop()
                visited[i] = False
            
dfs()