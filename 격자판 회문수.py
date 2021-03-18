
a = [list(map(int,input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]   
        if tmp == tmp[::-1]: # 역순 으로 앞뒤가 같은지 확인하는 방법
            cnt +=1
        for k in range(2):
            if a[i+k][j] != a[i+4-k][j]:
                break
        else:
            cnt+=1

print(cnt)


