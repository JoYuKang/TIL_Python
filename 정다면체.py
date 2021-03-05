
a,b = map(int,input().split())

n =[0]*(a+b+1)
for i in range(1,a+1):
    for j in range(1,b+1):
        n[i+j] +=1
max = 0
for i in range(1,a+b):
    if max <= n[i]:
        max = n[i]

    for i in range(a+b):
        if max ==n[i]:
           print(i,end=' ')