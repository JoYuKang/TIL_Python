num = int(input())

arr = [list(map(int,input().split())) for _ in range(num)]

#print(arr)
max = 0

for i in range(num):
    sum1 = sum2 = 0
    for j in range(num):
        sum1 += arr[i][j]
        sum2 += arr[j][i]
    if max < sum1:
        max = sum1
    if max <sum2:
        max = sum2

sum1 = sum2 = 0

for i in range(num):
    sum1 = arr[i][i]
    sum2 = arr[i][num-i-1]
if max < sum1:
    max = sum1
if max < sum2:
    max = sum2
print(max)