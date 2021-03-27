
n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    x = input()
    arr1.append(x)

for i in range(n-1):
    x = input()
    arr2.append(x)

arr1.sort()
arr2.sort()

for i in range(n):
    if(arr1[i] != arr2[i]):
        print(arr1[i])
        break