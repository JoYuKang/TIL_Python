n = int(input())

arr= list(map(int,input().split()))

m = int(input())

arr.sort()

for i in range(m):
    arr[len(arr)-1] -=1
    arr[0] +=1
    arr.sort()

print(arr[len(arr)-1] - arr[0])