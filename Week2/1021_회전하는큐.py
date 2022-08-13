
from collections import deque
import sys


n, m = map(int, sys.stdin.readline().strip().split())

arr = deque(map(int, sys.stdin.readline().strip().split()))

rotation = deque(x for x in range(1, n + 1))
#print(arr)
#print(rotation)
count = 0 
while arr:
    if arr[0] == rotation[0]:
        rotation.popleft()
        arr.popleft()
    else:
        temp = rotation.copy()
        front = 0
        back = 0 
        while arr[0] != temp[0]:
            front += 1
            temp.rotate(-1)
        temp = rotation.copy()
        while arr[0] != temp[0]:
            back += 1
            temp.rotate(1)
        if front > back:
            count += back
        else:
            count += front
        rotation = temp.copy()

print(count)
