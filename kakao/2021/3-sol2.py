import bisect
import time

def solution(info, query):
    t = time.time()
    ans = []

    infos = {}

    tmp = []
    for item in info:
        item = item.split()
        k, score = tuple(item[:4]), int(item[-1])
        tmp.append((k, score))

    tmp.sort(key=lambda x: x[1])

    for item in tmp:
        k, score = item
        if k not in infos:
            infos[k] = []
        infos[k].append(score)

    for q in query:
        q = q.split()
        q = list(filter(lambda x: x != 'and', q))
        q_score = int(q[-1])
        q = q[:-1]

        q_k = list(infos.keys())

        for current_q in q:
            if current_q == '-':
                continue
            q_k = list(filter(lambda x: current_q in x, q_k))

        q_infos = [infos[x] for x in q_k]
        q_result = 0

        for scores in q_infos:
            # idx = bisect.bisect_left(scores, q_score)
            # count = len(scores) - idx
            # q_result += count
            s = 0
            e = len(scores) - 1
            m = (e + s) // 2
            while True:
                if q_score <= scores[m]:
                    e = m
                else:
                    s = m + 1
                if m == ((e + s) // 2):
                    q_result += len(scores[s:])
                    break
                m = (e + s) // 2

        ans.append(q_result)

    return ans

info = ["java backend junior pizza 150", "python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
s = time.time()
print(solution(info, query))
print('t-time: ', time.time() - s)