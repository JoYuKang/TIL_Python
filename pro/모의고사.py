def solution(answers):
    answer = []
    num = [0,0,0]
    a = [ 1, 2, 3, 4, 5]
    b = [ 2, 1, 2, 3, 2, 4, 2, 5]
    c = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            num[0] +=1
        if answers[i] == b[i%len(b)]:
            num[1] +=1
        if answers[i] == c[i%len(c)]:
            num[2] +=1

    maxnum = max(num[0],num[1],num[2]) 

    for i in range(len(num)):
        if num[i] == maxnum:
            answer.append(i+1)

    return answer

answers = [ 1, 2, 3, 4, 5]
