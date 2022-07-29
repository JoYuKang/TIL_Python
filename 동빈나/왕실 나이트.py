
where = input()

y, x = ord(where[0]),int(where[1])

y = int(y - ord('a')) + 1
arr = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

result = 0

for i in arr:
    nx = x + i[0]
    ny = y + i[1]
    if ny <= 8 and ny >= 1 and nx <= 8 and nx >= 1:
        result += 1

print(result)
