import time

def solution(info, query):
    answer = []
    infos = {}
    # info 정리
    for ele in info:
        ele = tuple(ele.split())
        if ele[:-1] not in infos:
            infos[ele[:-1]] = []
        infos[ele[:-1]].append(int(ele[-1]))
    for k, v in infos.items():
        infos[k].sort()

    for ele in query:
        q_k = infos.keys()
        q = ele.replace('and', '').split()[:-1]
        cri = int(ele.replace('and', '').split()[-1])
        for c_q in q:
            if c_q == '-':
                continue
            q_k = list(filter(lambda x: c_q in x, q_k))
        # q_k 없는 경우도 생각
        q_result = 0
        for k in q_k:
            scores = infos[k]
            s = 0
            e = len(scores)
            while e > s:
                m = (e + s) // 2
                if cri <= scores[m]:
                    e = m
                else:
                    s = m + 1
            q_result += (len(scores) - s)
        answer.append(q_result)
    return answer



info = ["java backend junior pizza 150", "python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
s = time.time()
print(solution(info, query))
print('t-time: ', time.time()-s)