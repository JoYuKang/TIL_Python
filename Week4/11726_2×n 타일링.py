

import sys


num = int(sys.stdin.readline().strip())

result = [0, 1, 2, 3]

for i in range(4, num + 1):
    result.append(result[i - 1] + result[i - 2])

print(int(result[num] % 10007))
