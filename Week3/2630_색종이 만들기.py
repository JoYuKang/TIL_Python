
import sys


num = int(sys.stdin.readline().strip())

# 2차원 배열 입력받기 [list(map(int, input().split())) for _ in range(B)]
arr = [list(map(int , sys.stdin.readline().strip().split())) for _ in range(num)]

white = 0
blue = 0

def divideConquer(x,y,n):
    start = arr[x][y]
    global white, blue
    for i in range(x, x + n):
        for j in range(y, y + n):
            if start != arr[i][j]:
                divideConquer(x, y, n // 2)
                divideConquer(x + n // 2, y, n // 2)
                divideConquer(x, y + n // 2, n // 2)
                divideConquer(x + n // 2, y + n // 2, n // 2)
                return
    if start == 0:
        white += 1
    else:
        blue += 1


divideConquer(0,0,num)


print(white)
print(blue)