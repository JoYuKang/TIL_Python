

n, m = map(int, input().split())
arr =[]
def func(dep):
    if len(arr) == m:
        print(*arr)
    else:
        for i in range(1, n + 1):
            if arr:
                if arr[-1] > i:
                    continue
            arr.append(i)
            func(dep + 1)
            arr.pop()

func(0)