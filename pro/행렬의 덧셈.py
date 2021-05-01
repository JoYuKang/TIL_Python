def solution(arr1, arr2):
    answer = []
    for i in range(0,len(arr1)):
        tmp = []
        for j in range(0,len(arr1[0])):
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
    return answer

arr1=[[1,2],[2,3]]
arr2=[[3,4],[5,6]]	
print(solution(arr1, arr2))