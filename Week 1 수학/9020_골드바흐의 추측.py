arr = []
n = int(input())
for i in range(0,n):
    temp = int(input())
    arr.append(temp)

maxnum = max(arr) + 1

decimal = [False,False] + [True] * maxnum

for i in range(2, maxnum):
    if decimal[i]:
        for j in range(i + i, maxnum, i):
            decimal[j] = False

result = ""
for i in arr:
    min,max = i // 2, i // 2
    while min > 0:
        if decimal[min] and decimal[max]:
            result += f'{min} {max}\n'
            break
        else:
            min -= 1
            max += 1

print(result)
