def solution(left, right):
    answer = 0
    arr1 = []
    
    while left <=right:
        
        for i in range(1,left+1):
            if left % i == 0:
                arr1.append(i)
        if len(arr1) % 2==0:
            answer += left
        if len(arr1) % 2==1:
            answer -= left
        
        left +=1
        arr1 = []

    return answer

left = 13
right = 17
print(solution(left,right))