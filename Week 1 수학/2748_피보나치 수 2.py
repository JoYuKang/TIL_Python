n = int(input())

current = 1
previous = 0 

for i in range(1,n):
    current, previous = current + previous, current

print(current)
