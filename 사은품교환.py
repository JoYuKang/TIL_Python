
num = int(input())

for i in range(num):
    n, m = map(int, input().split())
    
    if n == 0:
        print(0)
        continue
    elif m == 0:
        print(n//12)
    else:
        total = (n+m) // 12
        season = n // 5
        if total == season:
            print(total)
        else:
            print(min(total, season))