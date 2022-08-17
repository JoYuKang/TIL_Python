
import heapq
import sys


n = int(sys.stdin.readline().strip())

heap = []

for i in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if not heap:
            print(0)
            continue
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)

