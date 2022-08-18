

n = int(input())

arr = list(map(int, input().split()))

result = [] 
# 최대값
stack = []

for i in range(len(arr)):
    while stack:
        if stack[-1][1] > arr[i]:
            result.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append([i + 1, arr[i]])
   

print(' '.join(map(str, result)))
