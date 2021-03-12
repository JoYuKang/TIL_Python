num = int(input())

arr = [list(map(int,input().split())) for _ in range(num)]

sum = 0

a = num//2

x = y = a

for i in range(num):
    for j in range(x,y+1):
        sum += arr[i][j]
    if i <num//2:
        x-=1
        y+=1
    else:
        x+=1
        y-=1

print(sum)