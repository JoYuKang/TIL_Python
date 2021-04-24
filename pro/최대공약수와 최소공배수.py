
def solution(n, m):
    answer = [0,0]
    answer[0] = gcd(n,m)
    answer[1] = lcm(n,m)

    return answer
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return a * b // gcd(a, b)
n = 3
m = 12
print(solution(n, m))