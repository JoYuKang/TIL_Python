def solution(n, k):

    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    num = rev_base[::-1] 

    arr = list(map(str, num.split('0')))

    answer = 0

    for i in arr:
        if not i:
            continue
        if isprime(int(i)):
            answer += 1

    return answer

def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

print(solution(110011, 10))