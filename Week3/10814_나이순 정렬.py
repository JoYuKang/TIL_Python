
import sys


n = int(sys.stdin.readline().strip())

arr = []
for i in range(n):
    arr.append(sys.stdin.readline().strip().split())

# 비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다.
# arr = sorted(arr,key = lambda arr : (arr[0], arr[1]))
arr = sorted(arr,key = lambda arr : int(arr[0]))
for i in arr:
    print(i[0],i[1])

