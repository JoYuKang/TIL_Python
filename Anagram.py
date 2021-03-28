n = input()
m = input()
n = list(n)
m = list(m)

n.sort()
m.sort()
a = 0
for i in range(len(n)):
    if n[i] !=m[i]:
        a = 1
        break
if a ==0:
    print("YES")
else:
    print("NO")


    