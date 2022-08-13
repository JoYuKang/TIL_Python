
from collections import deque
import sys


num = int(sys.stdin.readline().strip())

queue = deque()

for i in range(num):
    str = sys.stdin.readline().strip().split()
    if str[0] == "push_front":
        queue.appendleft(str[1])
    elif str[0] == "push_back":
        queue.append(str[1])
    elif str[0] == "pop_front":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif str[0] == "pop_back":
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif str[0] == "size":
        print(len(queue))
    elif str[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif str[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif str[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    