from heapq import heappop, heappush
def solution(n, k, enemy):
    answer = 0
    sumEnemy = 0
    heap = []

    for i in enemy :
        heappush(heap, -i)
        sumEnemy += i
        if sumEnemy > n:
            if k == 0:
                break
            sumEnemy += heappop(heap)
            k -= 1
        answer += 1

    return answer

print(solution(7,3,[4, 2, 4, 5, 3, 3, 1]))