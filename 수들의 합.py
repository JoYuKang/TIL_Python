n,m = map(int,input().split())


a = list(map(int,input().split()))
cnt = 0
lt = 0
rt = 1 
tot = a[0]
while 1:
    if tot<m:
        if rt<n:
            tot +=a[rt]
            rt+=1
        else:
            break
    elif tot ==m:
        cnt+=1
        tot -=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1

print(cnt)