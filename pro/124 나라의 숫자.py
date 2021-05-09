def solution(n):
    answer = ''
    num = ['4','1','2']
    while n > 0:
        remain = n%3 #remain = 1 
        n = n //3 # n = 3 
        if remain ==0:
            n = n-1
        answer += num[remain]
    answer = answer[::-1]
    return answer

n = 10
print(solution(n))