def solution(numbers):
    answer = 0
    for i in range(1,10):
      if i in numbers:
        continue
      else:
        answer += i

    return answer

print(solution([1,2,3,4,6,7,8,0]))