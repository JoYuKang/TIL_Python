
def solution(n):
    answer = ""

    while n >0:
        n, rest = divmod(n, 3)
        answer += str(rest)

    answer = int(answer, 3)

    return answer


n = 45

print(solution(n))