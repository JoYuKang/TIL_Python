

n,m = map(int,input().split())

arr= list(map(int,input().split()))


arr = sorted(arr)

visited = [False] * n

allArr = set()

printArr = []

checkNum = 0

def dfs():
    global checkNum
    if len(printArr) == m:
        allArr.add(tuple(printArr))
        #print(' '.join(map(str, printArr)))
    else:
        for i in range(0,len(arr)):
            if visited[i] == False:
                visited[i] = True
                printArr.append(arr[i])
                checkNum = arr[i]
                dfs()
                visited[i] = False
                printArr.pop()
                
dfs()

allArr = sorted(list(allArr))

for i in allArr:
    print(' '.join(map(str, i)))
