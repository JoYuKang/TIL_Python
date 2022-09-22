# 소수 구하기 방법 배열을 만들고 그 배열안의 소수 값으 True, False로 구한다.

# 배열 전체
def decimal(n):
    arr = [False,False] + [True] * (n + 1)

    for i in range(2, n+1):
        if arr[i] == True:
            for j in range(i + i, n + 1, i):
                arr[j] = False

    return arr

# 하나의 값만 찾기
def isprime(n):
    if n <= 1: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
