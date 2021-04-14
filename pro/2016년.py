
def solution(a,b):
    answer = ""
    arr= ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    ar = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = -1
    for i in range(0,a-1):
        date += ar[i]
    date += b
    answer += arr[date%7]
    return answer, date

a = 5
b = 24
print(solution(a,b))