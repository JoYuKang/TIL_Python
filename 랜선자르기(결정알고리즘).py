
n, m = map(int,input().split())

a = []
for i in range(n):
    x = int(input())
    a.append(x)

a.sort()


lt = 1
rt = a[len(a)-1]


while lt <= rt :
    sum = 0
    mid = (lt+rt)//2
    for i in a:
        sum += (i//mid)
    if sum < m :
        rt = mid - 1
    else :
        res = mid
        lt = mid + 1

print(res)