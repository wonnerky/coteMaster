# bfs
from collections import deque
import copy

def solution(sales, links):
    teams = {}
    for link in links:
        if link[0] not in teams:
            teams[link[0]] = [link[0]]
        teams[link[0]].append(link[1])
    select = [0 for _ in range(len(sales) + 1)]
    leaders = list(teams.keys())
    min_sum = 1e9
    idx = 0
    q = deque()
    for p in teams[leaders[idx]]:
        select_ = copy.deepcopy(select)
        c_sum = sales[p - 1]
        select_[p] = 1
        q.append([idx + 1, c_sum, select_])
    while q:
        idx, c_sum, select = q.popleft()
        # bfs, 현재까지 계산이 이미 min_sum 보다 높으면 패스
        if c_sum >= min_sum:
            continue
        # 모든 팀을 확인하면 min_sum 업데이트
        if idx == len(leaders):
            min_sum = min(c_sum, min_sum)
            continue
        # 팀에서 한 사람 선택하기
        for p in teams[leaders[idx]]:
            select_ = copy.deepcopy(select)
            if select_[p] == 0:  # 이미 선택된 사람이 아니면
                n_sum = c_sum + sales[p - 1]
                select_[p] = 1
                q.append([idx + 1, n_sum, select_])

            else:   # 이미 선택이 됐다면, 두 팀에 속했다는 것
                q.append([idx + 1, c_sum, select_])

    return min_sum



sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))