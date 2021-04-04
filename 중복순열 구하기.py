import sys


def DFS(l):
    global cnt
    if l ==m:
        for j in range(m):
            print(res[j],end=' ')
        print()
        cnt+=1 
    else:
        for i in range(1,n+1):
            res[l]=i
            DFS(l+1) 



n,m = map(int,input().split())
res = [0]*m
cnt = 0
DFS(0)
print(cnt)