def solution(storey):
    answer = 0
    while storey:
        remainder = storey % 10
        if remainder > 5:
            answer += 10 - remainder
            storey += 10
        elif remainder < 5:
            answer += remainder
        else : # 5인 경우 2번째 자리 비교
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10

    return answer

print(solution(16))