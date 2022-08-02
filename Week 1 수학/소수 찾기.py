
n = int(input())

arr = list(map(int,input().split()))

maxnum = max(arr) + 1 

decimal = [False,False] + [True] * maxnum

for i in range(2,maxnum):
    if decimal[i]:
        for j in range(i + i, maxnum, i):
            decimal[j] = False

result = 0

for i in arr:
    if decimal[i]:
        result += 1

print(result)




