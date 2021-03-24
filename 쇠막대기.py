st = input()

stack = []
sum = 0
for i in range(len(st)):
    if st[i] =='(':
        stack.append(st[i])
    else:
        if st[i - 1] =='(':
            stack.pop()
            sum += len(stack)
        else:
            stack.pop()
            sum += 1    

print(sum)