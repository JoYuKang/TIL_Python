

num = int(input())

arr = []

def decimalFunc(num):
    decimal = [False, False] + [True] * (num - 1)
    for i in range(2, num + 1):
        if decimal[i] == True:
            for j in range(i + i, num + 1, i):
                decimal[j] = False
    return decimal

decimal = decimalFunc(num)


for i in range(2, num + 1):
    if decimal[i]:
        arr.append(i)


answer = 0
p1 = 0
p2 = 1

while p1 < len(arr) and p2 <= len(arr):
    
    total = sum(arr[p1:p2])
    if total == num:
        answer +=1
        p2 += 1
    elif total > num:
        p1 += 1
    else:
        p2 += 1

    
print(answer)