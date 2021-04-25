def solution(n):
    answer = []
    while n!=0:
        x = n%10
        n = n//10
        answer.append(x)
    return answer

n = 12345
print(solution(n))