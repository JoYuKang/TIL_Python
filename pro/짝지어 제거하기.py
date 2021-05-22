

def solution(s):
    arr = []
    for i in s:    
        if len(arr) ==0:
            arr.append(i)
        else:
            if arr[-1] == i:
                arr.pop()
            else:
                arr.append(i)
    if len(arr) == 0:
        return 1
    else:
        return 0



s = "cdcd"
print(solution(s))