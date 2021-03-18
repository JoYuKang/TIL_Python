n, m = map(int,input().split())

arr =  list(map(int,input().split()))

def Count(mid):
    cnt = 1
    sum = 0
    for x in arr:
        if sum + x > mid:
            cnt +=1
            sum = x
        else:
            sum += x
    return cnt

maxx = max(arr)

lt = 1
rt = sum(arr)
while lt <= rt:
    mid = (lt+rt)//2
    if mid >= maxx and Count(mid) > m:   # 조건에 부합 X 
        res = mid     
        lt = mid + 1
    else:  #최소 용량 찾기 
        res = mid
        rt = mid - 1

print(res)