a = [5,6,8,7,1,2,9,0]
min = a[0]
for i in range(1,len(a)):
    if min >= a[i]:
        min = a[i]

print(min)