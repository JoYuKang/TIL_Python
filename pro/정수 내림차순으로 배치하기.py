def solution(n):
    answer = 0
    a = []
    while n !=0:
        a.append(n%10)
        n = n//10
    a.sort(reverse= True)
    for i in a:
        answer = i + answer*10
        print(answer)
    return answer


n = 118372
print(solution(n))