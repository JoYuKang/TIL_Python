import sys

n = int(input())
p = dict()
for i in range(n):
    x = input()
    p[x] = 1

for i in range(n-1):
    x = input()
    p[x] = 0

for key, val in p.items():
    if val == 1:
        print(key)
    