from collections import Counter
def solution(k, tangerine):
    answer = 0
    total = k
    cnt = Counter(tangerine)

    cntMost = cnt.most_common()
    # 빈도 값만 추출
    frequency_values = [count for _, count in cntMost]
    # 다른 방법
    # sorted(cnt.values(), reverse = True)
    for i in frequency_values:
        if k <= 0:
            break
        k -= i
        answer += 1

    return answer


print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))