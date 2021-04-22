def solution(s):
    answer = True
    s = s.lower()
    print(s)
    if s.count("p") == s.count("y"):
        return True

    
    return False

s = "Pyy"
print(solution(s))