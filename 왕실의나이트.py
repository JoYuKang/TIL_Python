data = input()

row = int(data[1])
# ord(c)는 문자의 아스키 코드 값을 돌려주는 함수이다.
column = int(ord(data[0])) - int(ord('a'))+1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

cnt = 0
for i in steps:
    next_row = row + i[0]
    next_column = column +i[1]
    if next_row >= 1 and  next_column >= 1 and next_row <= 8 and next_column <= 8 :
        cnt += 1

print(cnt)