# bfs 사용

from collections import deque
INF = int(1e9)
t = int(input())
result = []
for _ in range(t):
    n = int(input())
    costs = []
    for _ in range(n):
        costs.append(list(map(int, input().split())))
    grids = [[INF]*n for _ in range(n)]
    grids[0][0] = costs[0][0]
    # 우, 아래
    move = [(0,1), (1,0)]
    q = deque()
    q.append(((0, 0), costs[0][0]))
    while q:
        (x, y), cost = q.popleft()
        for i in range(2):
            nx, ny = x+move[i][0], y+move[i][1]
            if nx < n and ny < n:
                cos = cost + costs[nx][ny]
                if cos < grids[nx][ny]:
                    grids[nx][ny] = cos
                    q.append(((nx, ny), cos))

    result.append(grids[n-1][n-1])

for ele in result:
    print(ele)




