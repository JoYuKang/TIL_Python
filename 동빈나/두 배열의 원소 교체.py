
n,m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a =sorted(a)
b= sorted(b, reverse=True)

for i in range(m):
    a[i] = b[i]

print(sum(a))
