
def solution(n):
    answer = 0
    count = 1
     
    
    while True:
        max = pow(count, 2)
        if max <n:
            count +=1
        if max == n:
            count +=1
            answer = pow(count,2)
            break
        if max > n:
            return -1
        
        
    return answer

n = 1
print(solution(n))