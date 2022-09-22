
# 사각형의 원리 
# 1 2 3
# 2 2 3
# 3 3 3
# 1 2 3 2 2 3 3 3 3
# 으로 변환 시 목과 나머지의 값을 구한 후 둘 중 더 큰 값에 + 1 을 해주면 해당 위치의 값을 확인할 수 있다.
def solution(n, left, right):
    arr = []
    for i in range(left, right + 1):
        row = i / n
        col = i % n
        insertNum = row + 1 if row > col else col + 1
        arr.append(insertNum)
    return arr
