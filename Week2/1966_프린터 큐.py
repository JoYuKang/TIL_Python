
from collections import deque
import sys


num = int(sys.stdin.readline().strip())

result = []
for i in range(num):
    n, m = map(int, sys.stdin.readline().strip().split())
    queue = deque(map(int, sys.stdin.readline().strip().split()))
    target = deque()
    for i in range(n):
        target.append(i)
    target[m] = "target"
    count = 0
    while queue:
        if queue[0] == max(queue):
            count += 1
            check = target.popleft()
            queue.popleft()
            if check == "target":
                result.append(count)
                break
            
        else:
            queue.rotate(-1)
            target.rotate(-1)


for i in result:
    print(i)