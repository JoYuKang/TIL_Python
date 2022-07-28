
from tkinter import N


n = int(input())

arr = list(input().split())

x , y = 1, 1

for i in arr:
    if i == 'R' and x <= n :
        x += 1 
    elif i == 'L' and x > 1 :
        x -= 1
    elif i == 'U' and y > 1 :
        y -= 1
    elif i == 'D' and y <= n :
        y += 1

print(y,x)    
