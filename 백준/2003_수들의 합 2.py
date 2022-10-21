
n, m = map(int, input().split())

arr = list(map(int, input().split()))

p1 = 0 
p2 = 1

answer = 0
while p1 < len(arr) and p2 <= len(arr):

    total = sum(arr[p1:p2])
    if total == m:
        answer += 1
        p2 += 1
    elif total < m:
        p2 += 1
    else:
        p1 += 1


print(answer)