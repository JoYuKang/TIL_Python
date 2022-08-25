
arr = list(map(int, input().split()))

answer = [1,2,3,4,5]


while arr != answer:
    for i in range(4):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(*arr)

