
import sys


import heapq
import sys


n = int(sys.stdin.readline().strip())

heap = []
result = ""

for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if not heap:
            # print(0)
            result += "0\n"
            continue
        # print(heapq.heappop(heap)[1])
        result += f'{heapq.heappop(heap)[1]}\n'
    else:
        if num not in heap:
            heapq.heappush(heap, (abs(num), num))

print(result)
