

import sys


arr = list(sys.stdin.readline().strip())

num = int(sys.stdin.readline().strip())

extendArr = []

for i in range(num):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == 'P':
        arr.append(command[1])
    elif command[0] == 'L':
        if arr:
            extendArr.append(arr.pop())
    elif command[0] == 'D':
        if extendArr:
            arr.append(extendArr.pop())
    elif command[0] == 'B' :
        if arr:
            arr.pop()

arr.extend(reversed(extendArr))
print(''.join(map(str, arr))) 