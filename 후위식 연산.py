st = input()
stack = []
for x in st:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x =='+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2+n1))
        elif x =='-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2-n1))
        elif x =='*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2*n1))
        elif x =='/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(int(n2/n1))
        
print(stack.pop())
        