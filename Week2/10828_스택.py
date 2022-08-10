import sys


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    string = sys.stdin.readline().split()
    if string[0]== 'push':
        arr.append(string[1])
    elif string[0] == 'pop':
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    elif string[0] == 'size':
        print(len(arr))
    elif string[0] == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    else:
        if not arr:
            print(-1)
        else:
            print(arr[-1])