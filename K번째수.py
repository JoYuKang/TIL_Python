def solution(array, commands):
    answer = []
    for i in commands:
        a,b,c =i[0], i[1], i[2]
        x = array[a-1:b]
        x.sort()
        answer.append(x[c-1])

    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))