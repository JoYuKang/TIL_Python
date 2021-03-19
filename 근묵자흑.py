import sys
import math
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

answer = math.inf
# 가장 작은 숫자가 맨 앞일 때... 맨 뒤일 때까지.
start_idx = arr.index(min(arr))
for i in range(k):
	cnt = 1
	front, back = arr[:start_idx-i], arr[start_idx+k-i:]
	front_cnt = len(front) // (k-1) + (1 if len(front) % (k-1) else 0)
	back_cnt = len(back) // (k-1) + (1 if len(back) % (k-1) else 0)
	answer = min(answer, cnt + front_cnt + back_cnt)
print(answer)