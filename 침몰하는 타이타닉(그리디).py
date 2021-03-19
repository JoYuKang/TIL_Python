from collections import deque

n, m = map(int,input().split())

# 리스트를 사용할때 pop[0]은 효율이 좋진 않음
# 자료 이동으로 한칸식 전부 이동
arr = list(map(int,input().split()))

arr.sort()

arr = deque(arr)
cnt = 0

while arr:
    if len(arr) ==1:
        cnt +=1
        break
    if arr[0] + arr[-1] > m:
        arr.pop()
        cnt +=1
    else:
        # arr.pop(0) 리스트는 이렇게 가능
        # deque는 이렇게 사용
        arr.popleft()
        arr.pop()
        cnt +=1


print(cnt)