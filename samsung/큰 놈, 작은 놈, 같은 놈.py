T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result = ""
for test_case in range(1, T + 1):
    a, b = input().split()
    sign = ""
    if a > b:
        sign = ">"
    elif a < b:
        sign = "<"
    else:
        sign = "="
    result += "#" + str(test_case) + " " + sign + "\n"

print(result)
    
