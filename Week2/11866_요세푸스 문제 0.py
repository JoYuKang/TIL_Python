
from collections import deque
import sys


n, m = map(int, sys.stdin.readline().strip().split())

queue = deque()

for i in range(1, n + 1):
    queue.append(i)
result = []
while queue:
    for i in range(m - 1):
        queue.rotate(-1)
    result.append(queue.popleft())


print(f'<{", ".join(map(str,result))}>')



