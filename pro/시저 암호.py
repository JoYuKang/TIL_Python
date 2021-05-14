
def solution(s, n):
    s = list(s) 
    for i in range(len(s)): 
        # s[i] 가 대문자이면
        if s[i].isupper():
            # ord(c)는 문자의 유니코드 값을 돌려주는 함수
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) 
        # s[i] 가 소문자이면 
        elif s[i].islower(): 
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) 
    return "".join(s)

s = "AB"
n = 1
print(solution(s,n))