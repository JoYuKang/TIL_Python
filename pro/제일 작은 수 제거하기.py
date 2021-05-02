def solution(arr):
    answer = [-1]
    if len(arr) ==1:
        return answer
    s = min(arr)
    arr.remove(s)
    
    
    return arr

arr = [4,3,2,1]
print(solution(arr))