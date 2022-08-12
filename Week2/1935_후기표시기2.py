
import sys

def cal(x, y, str):
    if str == "+":
        return x + y
    elif str == "-":
        return x - y
    elif str == "*":
        return x * y
    elif str == "/":
        return x / y


n = int(sys.stdin.readline().strip())

text = list(sys.stdin.readline().strip())

num = [0] * n

for i in range(n):
    num[i] = int(sys.stdin.readline().strip())

stack = []

for i in range(len(text)):
    if  'A' <= text[i] <= 'Z':
        stack.append( num[ord(text[i]) - ord('A')])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(cal(num2,num1,text[i]))
    
print(f'{stack[0]:.2f}')





