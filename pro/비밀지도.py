def solution(n, arr1, arr2):
    answer = []
    for decimal1, decimal2 in zip(arr1, arr2):
        binary12 = str(bin(decimal1 | decimal2))[2:]
        binary12 = '0' * (n - len(binary12)) + binary12
        binary12 = binary12.replace('1', '#')
        binary12 = binary12.replace('0', ' ')
        answer.append(binary12)

    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))