
arr = list(range(21))
for i in range(10):
    a,b = map(int, input().split())
    for j in range((b-a+1)//2):
        arr[a+j],arr[b-j] = arr[b-j], arr[a+j]

arr.pop(0)
for i in arr:
    print(i,end=' ')