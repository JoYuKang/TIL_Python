

def solution(arr):
    answer = []
    a = arr[0]
    answer.append(a)
    for i in arr:
        if i != a:
            answer.append(i)
        a = i
    return answer

arr = [1,1,3,3,0,1,1]

print(solution(arr))