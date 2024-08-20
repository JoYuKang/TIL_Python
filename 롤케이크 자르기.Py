from collections import Counter

def solution(topping):
    answer = 0
    dic = Counter(topping)
    print(dic)
    tmp = set()
    for i in topping:
        dic[i] -= 1
        tmp.add(i)
        if(dic[i] == 0):
            dic.pop(i)
        if(len(dic) == len(tmp)):
            answer += 1

    return answer


print(solution([1, 2, 3, 1, 4]))