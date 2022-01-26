# 런타임 에러, 11라인에 아주 작은 값을 더해주는 것이 핵심
# list의 count 기능을 쓰면 좀 더 간결하게 만들 수 있음

def solution(N, stages):
    answer = {}
    stages.sort()
    cnt_stage = [0]*(N+2)
    for ele in stages:
        cnt_stage[ele] += 1
    for i in range(1, N+1):
        answer[i] = cnt_stage[i]/(sum(cnt_stage[i:])+1e-9)

    answer = dict(sorted(answer.items(), key=lambda item: item[1], reverse=True))
    return list(answer)


N = 4
stages = [4,4,4,4,4]
print(solution(N, stages))