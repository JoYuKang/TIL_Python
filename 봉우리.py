num = int(input())

arr = [list(map(int,input().split())) for _ in range(num)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

#위 아래 0으로 변환
arr.insert(0,[0]*num)
arr.insert(len(arr),[0]*num)

# 앞 뒤 0으로 변환
for i in arr:
    i.insert(0,0)
    i.append(0)

# for i in arr:
#     print(i)

cnt = 0

for i in range(1,num+1):
    for j in range(1,num+1):
        if all(arr[i][j]>arr[i+dx[k]][j+dy[k]] for k in range(4)): # k가 0부터 3까지 돌면서 x y좌표 확인
            cnt +=1

print(cnt)