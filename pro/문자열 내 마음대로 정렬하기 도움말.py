def solution(strings, n):
    answer = []
    a = []
    for i in range(len(strings)):
        answer.append(strings[i][n])
    answer.sort()
    
    for i in answer:
        for j in strings:
            if j[n] ==i:
                a.append(j)
    a = set(a)
    return a

strings = ["abce", "abcd", "cdx"]
n = 1

print(solution(strings, n))