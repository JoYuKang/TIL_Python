
import sys


num = sys.stdin.readline().strip()

arr = list(map(int, sys.stdin.readline().strip().split()))

check = sorted(list(map(int, set(arr))))

dic = {}

for i in range(len(check)):
    dic[check[i]] = i

for i in arr:
    print(dic[i],end=' ')


