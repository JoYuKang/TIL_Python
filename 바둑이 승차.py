
def DFS(L,sum,tsum):
    global result
    if sum +(total - tsum) < result:
        return
    if n < sum:
        return
    if L==m:
        if sum > result:
            result = sum
    else:
        DFS(L+1,sum+arr[L],tsum+arr[L])
        DFS(L+1,sum,tsum+arr[L])

n,m = map(int, input().split())
arr = [0]*m
result = 0

for i in range(m):
    arr[i] = int(input())
total = sum(arr)
DFS(0,0,0)
print(result)