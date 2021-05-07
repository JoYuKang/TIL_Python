def solution(x, n):
    answer = []
    count = 0
    while count != n:
        count += 1
        answer.append(x*count)

    return answer

x = -4
n = 2
print(solution(x, n))