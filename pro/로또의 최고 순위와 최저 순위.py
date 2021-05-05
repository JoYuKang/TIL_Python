def solution(lottos, win_nums):
    answer = [0,0]
    count = 0
    num = 0
    for i in lottos:
        if i ==0:
            count +=1
    if count == 6:
        return [1,6]
    for i in lottos:
        if i in win_nums:
            num +=1
    # answer[0]
    if num + count == 6:
        answer[0] = 1
    if num + count == 5:
        answer[0] = 2        
    if num + count == 4:
        answer[0] = 3        
    if num + count == 3:
        answer[0] = 4
    if num + count == 2:
        answer[0] = 5
    if num + count == 1:
        answer[0] = 6
    # answer[1]
    if num == 6:
        answer[1] = 1
    if num == 5:
        answer[1] = 2        
    if num == 4:
        answer[1] = 3        
    if num == 3:
        answer[1] = 4
    if num == 2:
        answer[1] = 5
    if num == 1:
        answer[1] = 6


    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))