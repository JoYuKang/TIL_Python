
arr = []
while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)

maxnum = max(arr) + 1

decimal = [False,False] + [True] * maxnum

for i in range(2, maxnum):
    if decimal[i]:
        for j in range(i + i, maxnum, i):
            decimal[j] = False

result = ""

for i in arr:
    sign = True
    for j in range(3,i,2):
        if decimal[j] and decimal[i - j]:
            result += f'{i} = {j} + {i - j}\n'
            sign = False
            break
    if sign:
        result += "Goldbach's conjecture is wrong./n"
print(result)
