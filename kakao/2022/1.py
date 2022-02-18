def solution(id_list, report, k):
    report = list(set(report))
    cnt = [0] * len(id_list)
    answer = [0] * len(id_list)
    for ele in report:
        cnt[id_list.index(ele.split()[1])] += 1
    for ele in report:
        if cnt[id_list.index(ele.split()[1])] >= k:
            answer[id_list.index(ele.split()[0])] += 1
    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

solution(id_list, report, k)