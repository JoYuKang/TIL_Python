n = int(input())

max= 0
for i in range(n):
    
    a = list(map(int,input().split()))
    a.sort()
    x,y,z = map(int,a)
    money =0
    if x==y and y==z:
        money = 10000+x*1000  
    elif x==y or x==z:
        money = 1000+x*100
        
    elif y==z:
        money = 1000+x*100
    else :
        money = z*100    
    if money>max:
        max =money    
print(max)