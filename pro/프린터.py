from collections import deque

def solution(priorities, location):
    answer = 0
    # enumerate는 리스트가 있는 경우 순서와 리스트의 값을 전달
    d = deque([(v,i) for i,v in enumerate(priorities)])
    while len(d):
        i = d.popleft()
        #(v, i) 중 v 값만 비교
        # d 없으면 런타임 에러
        if d and max(d)[0] > i[0]:
            d.append(i)
        else:
            answer += 1
            if i[1] == location:
                break

    return answer


priorities = [2, 1, 3, 2]
location = 2
print(solution(priorities, location))