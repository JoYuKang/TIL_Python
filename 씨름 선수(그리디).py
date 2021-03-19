n = int(input())

arr = []
for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))

arr.sort(reverse=True)

max = arr[0][1]
cnt = 0
for i in arr:
    if i[1]>= max:
        max = i[1]
        cnt +=1
    
print(cnt)

