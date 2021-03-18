n,m = map(int,input().split())

arr = list(map(int, input().split()))

lt = 0
rt = len(arr)-1

arr.sort()
mid = 0

while lt <= rt :
    mid = int((lt + rt)/2)
    if arr[mid] == m:
        break
    #  arr[mid] 의 값이 m보다 작으면 lt값을 mid +1을 해주어 작은 부분을 버린다
    elif arr[mid] < m:
        lt = mid + 1
    else:
        rt = mid - 1 

print(mid+1)