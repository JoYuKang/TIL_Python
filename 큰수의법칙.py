
x, y, z = map(int,input().split())

a = list(map(int,input().split()))

a.sort()
f = a[x-1] # 가장 큰수
s = a[x-2] # 두번째로 큰수
sum =0
while True:
    for i in range(z):
        if y ==0:
            break
        sum +=f
        y -=1
    if y ==0:
        break
    sum+=s
    y-=1    

print(sum)