import sys
n =int(input())

k = list(map(int, input().split()))

avg = round(sum(k)/n)

#print(avg)
min = 2410000000
for idx, x in enumerate(k):
    tmp = abs(avg-x)
    if min>tmp:
        min = tmp
        score = x
        res = idx+1
    elif min ==tmp:
        if x>score:
            score = x
            res = idx+1

print(avg, res)