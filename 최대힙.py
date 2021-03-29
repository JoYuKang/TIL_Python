import sys
import heapq as hq
# 힙의 자료구조화 시켜준다

a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n ==0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))
            # a에서 가장 작은 자료를 가져온다 
            # 힙구조면 root 노드값을 뽑는다
            # -를 붙여 -부분을 빼준다
    else:
        hq.heappush(a , -n)
        # a라는 리스트에 n값을 넣어준다
        # 최대 힙으로 넣어준다 -를 붙여줘서