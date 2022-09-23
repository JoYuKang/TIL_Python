

def solution(s):
    answer = []
    dic = {}
    arr = s[2:-2]

    arr = arr.split("},{")
    arr = sorted(arr, key=len)
    for i in arr:
        temp = i.split(',')
        for j in temp:
            if int(j) not in answer:
                answer.append(int(j))
    
    return answer


print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))