def solution(x):
    a = str(x)
    z = 0
    for i in a:
        z += int(i)
    #print(z)
    if x%z==0:
        return True
    else:
        return False
    

arr = 10
print(solution(arr))