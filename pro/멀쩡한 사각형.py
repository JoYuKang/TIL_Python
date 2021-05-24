def solution(w,h):
    answer = 1
    min = h
    max = w
    value = 1
    while value !=0:
        value = max %min
        max = min
        min = value
    answer = w * h -(w+h-max)
		# 선이 지나가면서 겹치는 사각형 개수는 블록 단위로 규칙적이다.
		#[2, 3] / [4, 6] / [6, 9] / [8, 12]
		
		# 블록의 크기는  (w / gcd) x  (h / gcd)  이다.
		# 한 블록 안에서는 (블록의 가로 크기 + 블록의 세로 크기 - 1) 수만큼의 사각형 위로 선이 지나간다.
    
		# 최대 공배수 구하는 방법
    return answer
    
w = 8
h = 12
print(solution(w,h))