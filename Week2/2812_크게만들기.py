

n, m = map(int, input().split())

num =  input()
stack = []
count = 0

for i in num:
    while stack:
        if stack[-1] < i and m > count:
            stack.pop()
            count += 1
        else:
            stack.append(i)
            break
    if not stack:
        stack.append(i)


print(''.join(stack[:n - m]))
    



