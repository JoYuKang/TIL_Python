

import sys


n = int(sys.stdin.readline())

for i in range(n):
    stack = []
    arr = list(sys.stdin.readline().strip())
    check = True
    for i in arr:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                check = False
                break
            stack.pop()
    if check and len(stack) == 0:
        print("YES")
    else:
        print("NO")

