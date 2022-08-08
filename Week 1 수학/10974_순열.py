
n = int(input())
arr = []
visited = [False] * (n + 1)
def dfs():
    if len(arr) == n:
        print(' '.join(map(str,arr)))
    else:
        for i in range(1 , n +1):
            if visited[i] == False:
                visited[i] = True
                arr.append(i)
                dfs()
                visited[i] = False
                arr.pop()
dfs()