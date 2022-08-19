

num = int(input())

arr = list(map(int,input().split()))

stack =[]
result = [-1] * num
arr = list(reversed(arr))

for i in range(num):
    while stack:
        if stack[-1] < arr[i]:
            stack.pop()
        else:
            result[i] = stack[-1]
            stack.append(arr[i])
            break
    if not stack:
        stack.append(arr[i])
            
           

print(*reversed(result))
