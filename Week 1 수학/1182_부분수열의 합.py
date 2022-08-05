

n,m = map(int, input().split())

arr= list(map(int, input().split()))

visit = []

result = 0
def dfs(count): 
    global result
    if len(visit) > 0 and sum(visit) == m:
        result +=1
    for i in range(count,n):
        visit.append(arr[i])
        dfs(i + 1)
        visit.pop()


dfs(0)

print(result)


