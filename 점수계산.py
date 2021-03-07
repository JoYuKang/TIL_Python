n = int(input())
arr = list(map(int,input().split()))
cnt = 0
sum = 0
for i in arr:
    if i ==1:
        cnt+=1
        sum+=cnt
    else:
        cnt=0
print(sum) 