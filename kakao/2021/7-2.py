# bfs
from collections import deque
import copy

def solution(sales, links):
    teams = {}
    my_team = [[] for _ in range(len(sales) + 1)]
    for link in links:
        if link[0] not in teams:
            teams[link[0]] = [link[0]]
            my_team[link[0]].append(link[0])
        teams[link[0]].append(link[1])
        my_team[link[1]].append(link[0])
    select = [0 for _ in range(len(sales) + 1)] # team
    leaders = list(teams.keys())
    min_sum = 0
    for p in leaders:
        if p == 1:
            continue
        min_sum += sales[p - 1]
    idx = 0
    q = deque()
    for p in teams[leaders[idx]]:
        select_ = copy.deepcopy(select)
        c_sum = sales[p - 1]
        for t in my_team[p]:
            select_[t] = 1
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
        # 이미 선택된 팀이면 다음 팀으로 넘어가기
        if select[leaders[idx]]:
            q.append([idx + 1, c_sum, select])
        else:
            for p in teams[leaders[idx]]:
                select_ = copy.deepcopy(select)
                n_sum = c_sum + sales[p - 1]
                for t in my_team[p]:
                    select_[t] = 1
                q.append([idx + 1, n_sum, select_])

    return min_sum



sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))