


def solution(p):
    answer = ''
    arr = []
    for i in p:
        if i =="(":
            arr.append(i)
        else :
            answer += arr.pop()
            answer += i
    return answer


p = "(()())()"
print(solution(p))