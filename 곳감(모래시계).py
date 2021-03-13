a = int(input())
arr1 = [list(map(int,input().split())) for _ in range(a)]
              
b = int(input())

for i in range(b):
    x, y, z = map(int,input().split())
    if y==0:
        for _ in range(z):
            arr1[x-1].append(arr1[x-1].pop(0))
    else:
        for _ in range(z):
            arr1[x-1].insert(0,arr1[x-1].pop())

#for x in arr1:
#    print(x)
sum = 0
k =0
t =a-1
for i in range(a):
    for j in range(k,t+1):
        sum += arr1[i][j]
    if i <a//2:
        k+=1
        t-=1
    else:
        k-=1
        t+=1
  
print(sum)