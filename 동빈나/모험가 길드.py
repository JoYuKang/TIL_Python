
num = int(input())
arr = list(map(int,input().split()))

arr = sorted(arr)
result = 0
count = 0 

for i in arr:
    count += 1
    if count >= i:
        result += 1
        count = 0


print(result)
