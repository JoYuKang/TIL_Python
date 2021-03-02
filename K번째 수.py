import sys


t = int(input())
for i in range (t):
    n, s, e, k = map(int,(input().split()))
    z = list(map(int, input().split()))    
    z = z[s-1:e]
    z.sort()
    print('#',i+1 ,z[k-1])