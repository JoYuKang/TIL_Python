


from os import replace


def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(10):
        if (arr[i] in s):
            s = s.replace(arr[i], str(i))
    return int(s)


s = "one4seveneight"
print(solution(s))