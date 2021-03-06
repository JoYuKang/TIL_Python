num = input()

a = list(map(int, input().split()))
arr = [0]*1000001
arr[0] = 1;
def isPrime(x):
    if x ==1:
        return False
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    else:
        return True
        
def reverse(x):
    res = 0
    while x>0:
        tmp = x%10
        res = res*10+tmp
        x = x//10
    return res

for i in range(0,len(a)):
    de = reverse(a[i])
    if isPrime(de) ==True:
        print(de, end = ' ')
    