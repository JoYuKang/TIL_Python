
def solution(s):
    answer = 0
    q = []
    z = []
    k = len(s)-1
    max = -1
    if s.count("(") != s.count(")"):
        return 0
    if s.count("[") != s.count("]"):
        return 0
    if s.count("{") != s.count("}"):
        return 0
    for j in range(0,len(s)):
        z.clear()
        if k == -1:
            break
        for i in range(k,len(s)-k):
            z.append(s[i])    
        print(z)
        answer = 0
        for i in z:
            if i == "[":
                q.append(i)
            elif i == "]":
                if "[" in q :
                    answer += 1
                    if "{" in q:
                        answer -=1
                    q.remove("[") 
            elif i == "(":
                q.append(i)
            elif i == ")":
                if "(" in q:
                    answer += 1 
                    q.remove("(")
            elif i == "{":
                q.append(i)
            elif i == "}":
                if "{" in q:
                    answer += 1 
                    if "["  in q:
                        answer -=1
                    q.remove("{")
        if max < answer:
            max = answer
        print(max , answer)
        if k <len(s):
            k -= 1
        q.clear()
        
    return max


s = "[](){}"
print(solution(s))
