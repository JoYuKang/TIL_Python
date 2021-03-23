
num, m = map(int,input().split())

num = list(map(int, str(num)))
stack =[]
for x in num:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)
if m != 0:
    stack = stack[:-m] # 제일 앞에서부터 뒤쪽 m개 날린다
# JOIN을 사용해서 STACK에 있는 값을 하나하나 더한다
res = ''.join(map(str,stack))

# for i in stack:
#     print(i,end='')

print(res)