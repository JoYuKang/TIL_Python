n,m = map(int, input().split())

result = 0
for i in range(n):
    arr = list(map(int,input().split()))
    minNum = min(arr)
    result = max(result, minNum)
    
print(result)
