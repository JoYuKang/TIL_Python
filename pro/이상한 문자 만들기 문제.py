def solution(s):
    answer = ''
    z = s.split(" ")
    #print(z)
    #print(len(z[1]))
    for j in range(0,len(z)):
        for i in range(0,len(z[j])):
            if i % 2 ==0:
                answer += z[j][i].upper()  
            else:
                answer += z[j][i].lower()
        if(j!=len(z)-1):
            answer+=" ";
              
    return answer

s = "try hello world"
print(solution(s))