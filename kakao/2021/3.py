def solution(info, query):
    answer = []
    # idx 정보 저장
    idxs={'cpp': [], 'java': [], 'python': [], 'backend': [], 'frontend': [],
          'junior': [], 'senior': [], 'chicken': [], 'pizza': []}
    for i in range(len(info)):
        for ele in info[i].split()[:-1]:
            idxs[ele].append(i)
    # 점수 제외, 각 조건의 조합은 108개. 정보 저장하면 더 편할 듯?
    for q in query:
        q = q.replace('and','').split()
        result = [i for i in range(len(info))]

        for ele in q[:-1]:
            if ele == '-':
                continue
            result = list(set(result) & set(idxs[ele]))

        # binary search
        cnt = 0
        for i in result:
            if int(info[i].split()[-1]) >= int(q[-1]):
                cnt += 1
        answer.append(cnt)
    return answer




info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))