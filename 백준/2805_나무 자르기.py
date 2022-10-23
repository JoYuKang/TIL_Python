
n,m = map(int, input().split())

arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0

while start <= end:
    mid = int((start + end) / 2)
    sum = 0 
    for i in arr:
        if i - mid > 0:
            sum += i - mid
    if m > sum:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)


