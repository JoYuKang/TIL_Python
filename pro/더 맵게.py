
import heapq

def solution(scoville, k):
    heapq.heapify(scoville)
    answer = 0
    while scoville[0] < k:
        if len(scoville) > 1:
            # 가장 작은원소 하나 빼고 그다음 가장 작은원소 하나 빼서 곱한 후 heqpq에 넣어준다.
            #  1 + (2 * 2) = 5
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
        else: # 만약 len(scoville) 가 1이면 k이상의 스코빌 지수를 만들 수 없어 -1을 리턴한다.
            return -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))