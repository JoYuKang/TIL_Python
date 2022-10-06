from typing import Counter


def solution(str1, str2):
    
    strArr1 = []
    strArr2 = []
    union = []
    intersection = []
    str1 = str1.lower()
    str2 = str2.lower()

    for i in range(0,len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha(): 
            strArr1.append(str1[i] + str1[i + 1])
    for i in range(0,len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha(): 
            strArr2.append(str2[i] + str2[i + 1])

    Counter1 = Counter(strArr1)
    Counter2 = Counter(strArr2)

    intersection = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    if len(intersection) > 0 and len(union) == 0:
        return 0

    if len(intersection) == 0 and len(union) == 0:
        return 65536
    
    
    return int(len(intersection) / len(union) * 65536)

print(solution("A+C", "DEF"))