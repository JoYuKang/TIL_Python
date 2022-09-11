def solution(n):
    
    
    arr = [0, 1, 2] + [0] * (n -2)

    for i in range(3,len(arr)):
        arr[i] = arr[i - 1] + arr[i - 2]
    

    return arr[n] % 1234567

print(solution(0))