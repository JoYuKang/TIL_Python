
from collections import deque
import sys


n = int(sys.stdin.readline().strip())

queue = deque()

for i in range(1, n + 1):
    queue.append(i)

count = 1

while len(queue) > 1:
    if count % 2 == 1:
        queue.popleft()
    else:
        queue.append(queue.popleft())
    count += 1
print(queue[0])
        

