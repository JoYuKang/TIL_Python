
def solution(cards1, cards2, goal):
    while goal:
        if len(cards1) > 0 and goal[0] == cards1[0]:
            goal.pop(0)
            cards1.pop(0)
        elif len(cards2) > 0 and goal[0] == cards2[0]:
            goal.pop(0)
            cards2.pop(0)
        else:
            return "No"
    return "Yes"


print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
