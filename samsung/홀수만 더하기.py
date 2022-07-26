T = int(input())
result = ""
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    inputlist = [int(x) for x in input().split()]
    # num_list = list(map(int, input().split()))
    sum = 0
    for i in inputlist:
        if i % 2 == 1:
            sum += i
    result += "#" + str(test_case) + " " + str(sum) + "\n"

print(result)
