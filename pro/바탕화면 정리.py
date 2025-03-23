def solution(wallpaper):
    answer = [0, 0, 0, 0]
    minX = 50
    minY = 50
    maxX = 0
    maxY = 0

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                minX = min(minX, i)
                minY = min(minY, j)
                maxX = max(maxX, i)
                maxY = max(maxY, j)

    answer[0] = minX
    answer[1] = minY
    answer[2] = maxX + 1
    answer[3] = maxY + 1

    return answer


print(solution([".#...", "..#..", "...#."]))