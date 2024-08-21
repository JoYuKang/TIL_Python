
def solution(keyinput, board):

    maxX = board[0] // 2
    minX = -maxX
    maxY = board[1] // 2
    minY = -maxY


    x = 0
    y = 0
    for i in keyinput :
        if i == "left" and x > minX:
            x -= 1
        elif i == "right" and x < maxX:
            x += 1
        elif i == "up" and y < maxY:
            y += 1
        elif i == "down" and y > minY:
            y -= 1
    answer = [x, y]
    return answer


print(solution(["down", "down", "down", "down", "down"], [7, 9]))