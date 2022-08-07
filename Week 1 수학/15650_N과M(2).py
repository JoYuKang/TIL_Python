
n, m = map(int, input().split())


arr = []
visit = [False] * (n+1)

def dfs():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
    else:
        for i in range(1,n + 1):
            if visit[i] == False:
                if len(arr) != 0:
                    if i < arr[-1]:
                        continue
                arr.append(i)
                visit[i] = True
                dfs()
                arr.pop()
                visit[i] = False
                

dfs()
