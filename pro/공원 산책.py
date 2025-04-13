def solution(park, routes):
    h = len(park)
    w = len(park[0])

    # 시작 위치 찾기
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                nowX, nowY = i, j

    for route in routes:
        d, r = route.split()
        r = int(r)
        can_move = True

        for step in range(1, r + 1):
            if d == 'E':
                ny = nowY + step
                if ny >= w or park[nowX][ny] == 'X':
                    can_move = False
                    break
            elif d == 'W':
                ny = nowY - step
                if ny < 0 or park[nowX][ny] == 'X':
                    can_move = False
                    break
            elif d == 'S':
                nx = nowX + step
                if nx >= h or park[nx][nowY] == 'X':
                    can_move = False
                    break
            elif d == 'N':
                nx = nowX - step
                if nx < 0 or park[nx][nowY] == 'X':
                    can_move = False
                    break

        if can_move:
            if d == 'E':
                nowY += r
            elif d == 'W':
                nowY -= r
            elif d == 'S':
                nowX += r
            elif d == 'N':
                nowX -= r

    return [nowX, nowY]


print(solution(	["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]))