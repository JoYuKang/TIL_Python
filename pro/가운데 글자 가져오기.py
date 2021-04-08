def solution(s):
    answer = ''
    a = 1
    if len(s) % 2 ==0:
        a = 2
        answer += s[len(s)//2-1:len(s)//2+1]
    else:
        answer += s[len(s)//2:len(s)//2+1]
    return answer


s = "abcde"
# print(s[int(len(s)//2):int(len(s)//2+1)])
print(solution(s))
