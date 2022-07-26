T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
result = ""
for test_case in range(1, T + 1):
    inputlist = [int(x) for x in input().split()]
    # num_list = list(map(int, input().split()))
    avg = round(sum(inputlist) / len(inputlist))
    result += "#" + str(test_case) + " " + str(avg) + "\n"

print(result)
    
