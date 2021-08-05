
def solution(price, money, count):
    answer = -1
    max = 0
    for i in range(1,count+1):
        max += price*i
    
    if max >= money:
        answer = max - money
    elif money > max:
        return 0 
    
    return answer
    


price = 3
money = 20
count = 3

print(solution(price,money,count))