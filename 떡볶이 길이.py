n,m = map(int,input().split())

arr = list(map(int,input().split()))

start = 0
end = max(arr)

result = 0

while start <= end:
    total = 0
    mid = (start + end)//2
    for x in arr:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1 
        break

print(result)
        