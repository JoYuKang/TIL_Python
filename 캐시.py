
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()

    if cacheSize == 0:
        return 5 * len(cities)


    for city in cities:
        temp = city.lower()
        if not queue:
            queue.append(temp)
            answer += 5
        else:
            if not queue.__contains__(temp):
                queue.append(temp)
                if len(queue) > cacheSize:
                    queue.popleft()
                answer += 5
            elif queue.__contains__(temp):
                queue.remove(temp)
                queue.append(temp)
                answer += 1

    return answer


print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))

