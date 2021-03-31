import sys

def DFS(L,sum):
    if sum > total//2:
        return
        
    if L == n :
        if sum ==(total)-sum:
            print("YES")
            sys.exit(0)

    else:
        DFS(L+1,sum+arr[L])
        DFS(L+1,sum)





n = int(input())

arr = list(map(int,input().split()))

total = sum(arr)
DFS(0,0)
print("NO")