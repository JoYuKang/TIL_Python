

n,m = map(int, input().split())

arr = [False,False] + [True] * (m + 1)

for i in range(2, m+1):
    if arr[i] == True:
        for j in range(i + i,m+1,i):
            arr[j] = False
result = ""
for i in range(n,m+1):
    if arr[i]:
        result += str(i) +"\n"

print(result)
        

