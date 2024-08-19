def solution(elements):
    answer = set()
    listLen = len(elements)
    elements = elements * 2

    for i in range(listLen) :
        for j in range(listLen) :
            answer.add(sum(elements[j:j+i:1]))

    return len(answer)

print(solution([7,9,1,1,4]))