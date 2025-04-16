def solution(n, m, section):
    answer = 0
    now = 0

    for i in section:
        if i > now:
            now = m + i - 1
            answer += 1

    return answer



print(solution(8, 4, [2, 3, 6]))