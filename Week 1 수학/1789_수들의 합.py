
n = int(input())

sum = 0
result = 0

for i in range(1, n + 1):
     sum += i
     result += 1
     if n < sum:
        result -= 1
        break
print(result)