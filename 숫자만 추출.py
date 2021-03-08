

st = input()

sum =0
for i in st:
    if i.isdecimal():
        sum = sum*10 +int(i)

print(sum)
cnt = 0
for i in range(1,sum+1):
    if sum%i==0:
        cnt =cnt+1
print(cnt)