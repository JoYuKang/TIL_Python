

num = int(input())

arr = list(map(int,input().split()))

stack =[]
result = [-1] * num


for i in range(len(arr)):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)
            
print(*result)
