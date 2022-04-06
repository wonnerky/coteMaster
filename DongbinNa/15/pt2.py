from collections import deque

N, M, K, X = map(int, input().split())
roads = [[] for _ in range(N+1)]
for _ in range(M):
    s, t = map(int, input().split())
    roads[s].append(t)
visit = [False] * (N + 1)
q = deque()
q.append((X, 0))
visit[X] = True
result = []
while q:
    s, cnt = q.popleft()
    if cnt > K:
        break
    if cnt == K:
        result.append(s)
    for t in roads[s]:
        if not visit[t]:
            visit[t] = True
            q.append((t, cnt + 1))

if result:
    result.sort()
    for ele in result:
        print(ele)
else:
    print(-1)

