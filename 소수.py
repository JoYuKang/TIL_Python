arr = [0]*1000001
arr[1]=1
num = int(input())
count = 0
for i in range(2,num+1):
    if arr[i]==0:
        count+=1
        for j in range(i,num+1,i):
            arr[j] = 1;


for i in range(2,num+1):
    if arr[i] !=1:
        count +=1

print(count)
