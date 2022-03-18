from collections import deque
# 중복된 항공권 있음
def solution(tickets):
    tickets.sort(key = lambda x:x[1])
    l = len(tickets)
    q = deque()
    s = 'ICN'
    for i in range(len(tickets)):
        if tickets[i][0] == s:
            q.append([i])
    while q:
        lst = q.popleft()
        if len(lst) == l:
            break
        idx = lst[-1]
        for i in range(len(tickets)):
            if i not in lst and tickets[idx][1] == tickets[i][0]:
                q.append(lst + [i])
    answer= ['ICN']
    for i in lst:
        answer.append(tickets[i][1])
    return answer



tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))