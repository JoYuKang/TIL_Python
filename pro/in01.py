def solution(code, day, data):
    answer = []
    if code in data:
        print(code)
    for i in data:
        if code in data:
            answer.append(i)

    return answer

company_code = "012345"
day = "20190620"
data = ["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014"
,"price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]

print(solution(company_code, day, data))