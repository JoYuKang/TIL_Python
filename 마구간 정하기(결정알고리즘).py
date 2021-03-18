n, m = map(int,input().split())
a = []
for i in range(n):
    tmp = int(input())
    a.append(tmp)


def Count(len):
    cnt = 1
    ep = a[0]
    for i in range(1,n):
        if a[i] - ep >=len:
            cnt +=1
            ep = a[i]       
    return cnt

a.sort()
lt = 1
rt = a[n - 1]

while lt <= rt :
    mid = (lt + rt) //2
    if Count(mid) >= m :
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1


print(res)