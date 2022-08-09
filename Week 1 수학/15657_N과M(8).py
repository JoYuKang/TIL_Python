

n,m = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr)
printArr = []
allArr = set()
tempNum = 0
def dfs(count):
    global tempNum
    if len(printArr) == m:
        allArr.add(tuple(printArr))
        # print(' '.join(map(str,printArr)))
    else:
        for i in range(count, len(arr)):
            tempNum = arr[i]
            printArr.append(arr[i])
            dfs(i)
            printArr.pop()

dfs(0)

allArr = sorted(list(allArr))

for i in allArr:
    print(' '.join(map(str, i)))