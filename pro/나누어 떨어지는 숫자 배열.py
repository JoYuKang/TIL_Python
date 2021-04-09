def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) >0:
        answer.sort()
    else:
        answer.append(-1)
    return answer


arr = [5, 9, 7, 10]
divisor = 5

print(solution(arr,divisor))