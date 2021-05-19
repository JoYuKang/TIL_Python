def solution(phone_number):
    answer =  "*" * (len(phone_number) - 4 )
    
    answer += phone_number[len(phone_number) -4:len(phone_number)]
    return answer

phone_number = "01033334444"
print(solution(phone_number))