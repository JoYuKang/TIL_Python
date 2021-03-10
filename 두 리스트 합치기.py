a = input()
arr1 = list(map(int,input().split()))
b = input()
arr2 = list(map(int,input().split()))

for i in arr2:
    arr1.append(i)

arr1.sort()
for i in arr1:
    print(i,end=' ')