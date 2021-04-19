def solution(absolutes, signs):
    answer = 0
     for i in range(0,len(signs)):
            if signs[i] == 1:
            answer += absolutes[i]
        elif signs[i] ==0:
            answer -= absolutes[i]
    
    return answer


absolutes = [4,7,12]
signs = [true,false,true]
