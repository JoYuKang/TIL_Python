
import sys


n = int(sys.stdin.readline().strip())

arr = []

for i in range(n):
    text = sys.stdin.readline().strip()
    sum = 0
    for j in text:
        if j.isdigit():
            sum += int(j)
    arr.append([text,sum])

arr = sorted(arr, key = lambda arr : (int(len(arr[0])), arr[1], arr[0]) )

for i in arr:
    print(i[0])