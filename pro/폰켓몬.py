def solution(nums):
    answer = 0
    arr= []
    arr = set(arr)

    a = len(nums)//2
    for i in nums:
        if len(arr) < a:
            arr.add(i)
    answer = len(arr)

    return answer

nums = [3,1,2,3]
print(solution(nums))