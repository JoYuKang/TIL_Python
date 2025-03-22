
def convertTime(n): # 분 단위로 변환
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(schedules)):
        flag = True
        schedule = convertTime(schedules[i])
        checkDay = startday
        for j in timelogs[i]:
            if checkDay in [6, 7]:
                checkDay += 1
                if checkDay > 7:
                    checkDay = 1
                continue
            if schedule + 10 < convertTime(j):
                flag = False
                break
            else:
                checkDay += 1
        if flag:
            answer += 1

    return answer


print(solution([700, 800, 1100], [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]], 5))