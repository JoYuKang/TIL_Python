from collections import deque


n,m = map(int,input().split())

arr = [(pos,val) for pos, val in enumerate(list(map(int,input().split())))]

arr = deque(arr)

cnt = 0

while 1:
    cur = arr.popleft()
    # ANY , ALL의 반대
    if any(cur[1] < x[1] for x in arr):
        arr.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break

    
    

    



