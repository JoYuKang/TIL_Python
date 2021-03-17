x,y = map(int,input().split())

result = 0
for i in range(x):
    arr = list(map(int,input().split()))
    min_value = min(arr)
    result = max(result,min_value)

print(result)