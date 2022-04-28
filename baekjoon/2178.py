# 최단 거리기 때문에!! a->b로 가는 여러 경우 생각 안하고, 처음 도달하는 것으로 퉁 쳐도 됨!

from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = [input() for _ in range(N)]

mov = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visit = [[False] * M for _ in range(N)]
visit[0][0] = True
q = deque()
q.append([(0, 0), 1])
while q:
    (x, y), cnt = q.popleft()
    if x == N - 1 and y == M - 1:
        break
    for i in range(4):
        nx, ny = x + mov[i][0], y + mov[i][1]
        if 0 <= nx < N and 0 <= ny < M:
            if not visit[nx][ny] and board[nx][ny] == '1':
                q.append([(nx, ny), cnt + 1])
                visit[nx][ny] = True
print(cnt)

