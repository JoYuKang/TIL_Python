

def solution(survey, choices):
    answer = ''
    dic = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0,  "N" : 0}

    for i in range(len(survey)):
        first = survey[i][0]
        secend = survey[i][1]
        checkNum = choices[i] - 4
        if checkNum > 0:
            dic[secend] += checkNum
        else:
            dic[first] += abs(checkNum)
            
    answer += "R" if dic["R"] >= dic["T"] else "T"
    answer += "C" if dic["C"] >= dic["F"] else "F"
    answer += "J" if dic["J"] >= dic["M"] else "M"
    answer += "A" if dic["A"] >= dic["N"] else "N"


    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]


print(solution(survey, choices))