def solution(name, yearning, photo):
    answer = []
    mapped_dict = dict(zip(name, yearning))

    for i in range(len(photo)):
        num = 0
        for j in photo[i]:
            value = mapped_dict.get(j, 0)
            num += value
        answer.append(num)

    return answer



print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))