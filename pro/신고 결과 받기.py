def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))
    reports = {x : 0 for x in id_list}
    reporter = {}
    reportedPlayer = {}
    for i in report:
        temp = i.split()
        if temp[0] not in reporter:
            reporter[temp[0]] = set()
        reporter[temp[0]].add(temp[1])

        if temp[1] not in reportedPlayer:
            reportedPlayer[temp[1]] = set()
        reportedPlayer[temp[1]].add(temp[0])

    for j in range(len(id_list)):
        if id_list[j] not in reporter:
                continue
        for x in reporter[id_list[j]]:
            if len(reportedPlayer[x]) >= k:
                answer[j] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))