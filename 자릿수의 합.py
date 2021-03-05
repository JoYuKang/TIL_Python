

a = int(input())

s = list(map(int,input().split()))
max = 0

# INT 형으로 하는 방법
def sum_int(num):
    sum = 0
    while num>0:
        sum += num%10
        num = num//10
    return sum
#print(s)

# STR형으로 하는 방법
def sum_str(num):
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum
#print(s)

for i in s:
    if max< sum_str(i):
        max = sum_str(i)
        count = i
        
print(count)
    