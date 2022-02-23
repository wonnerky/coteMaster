from collections import deque
N, M, K, X = map(int, input().split())
road = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    road[a].append(b)

dist = [-1] * (N+1)
dist[X] = 0
q = deque()
q.append((X, 0))
while q:
    idx, d = q.popleft()
    d += 1
    for i in road[idx]:
        if dist[i] == -1:
            q.append((i, d))
            dist[i] = d
result = []
for i in range(1, N + 1):
    if dist[i] == K:
        result.append(i)
if result:
    for ele in result:
        print(ele)
else:
    print(-1)