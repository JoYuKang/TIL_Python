
from collections import deque
import sys


num = int(sys.stdin.readline().strip())

queue = deque()
result = ""
for i in range(num):
    input = sys.stdin.readline().strip().split()
    if input[0] == "push":
        queue.append(input[1])
    elif input[0] == "pop":
        if queue:
            result += queue.popleft() + "\n"
        else:
            result += "-1\n"
    elif input[0] == "size":
        result += str(len(queue)) + "\n"
    elif input[0] == "empty":
        if queue:
            result += "0\n"
        else:
            result += "1\n"
    elif input[0] == "front":
        if queue:
            result += queue[0]  + "\n"
        else:
            result += "-1\n"
    elif input[0] == "back":
        if queue:
            result += queue[-1] + "\n"
        else:
            result += "-1\n"

print(result)