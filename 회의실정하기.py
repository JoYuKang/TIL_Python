num = int(input())
arr = []
for i in range(num):
    n,m = map(int,input().split())
    arr.append((n,m))

# 뒤를 중심으로 정렬
arr.sort(key = lambda x : (x[1],x[0]))

endtime = 0
cnt = 0
# 시작 , 끝
for s,e in arr:
    if s >= endtime:
        cnt +=1
        endtime = e


print(cnt)