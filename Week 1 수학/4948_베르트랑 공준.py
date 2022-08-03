arr = []
while True:
    n = int(input())
    if n == 0:
        break
    arr.append(n)

maxnum = (max(arr)+1) * 2

decimal = [False, False] + [True] * (maxnum)

result = ""

for i in range(2, maxnum + 1):
    if decimal[i]:
        for j in range(i+i,maxnum+1,i):
            decimal[j] = False

for i in arr:
    count = 0
    for j in range(i + 1 , i * 2 + 1):
        if decimal[j]:
            count += 1
    result += str(count) + "\n"

print(result)

