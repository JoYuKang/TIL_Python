def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings
strings = ["abce", "abcd", "cdx"]
n = 1

print(solution(strings, n))