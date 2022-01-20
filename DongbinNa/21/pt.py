# queue 사용
# 최대 2500번 재귀 사용.. maximum 1000
# dfs 함수 사용 안하는 방법으로 진행...?

import sys
from collections import deque


def solution():
    input = sys.stdin.readline
    n, l, r = map(int, input().split())

    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))

    # 좌 위 우 아래
    dx = [0, -1, 0, 1]  # 위 아래
    dy = [-1, 0, 1, 0]  # 좌 우
    days = 0

    while True:
        visited = [[0] * n for _ in range(n)]
        unions = []
        for i in range(n):
            for j in range(i%2, n, 2):
                if visited[i][j] == 0:
                    q = deque()
                    q.append((i,j))
                    union = []
                    visited[i][j] = 1
                    union.append((i, j))
                    total_pop = A[i][j]
                    while q:
                        x, y = q.popleft()
                        for idx in range(4):
                            nx = x + dx[idx]
                            ny = y + dy[idx]
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                                if l <= abs(A[x][y] - A[nx][ny]) <= r:
                                    total_pop += A[nx][ny]
                                    union.append((nx, ny))
                                    q.append((nx, ny))
                                    visited[nx][ny] = 1
                    if len(union) > 1:
                        new_pop = total_pop // len(union)
                        for x, y in union:
                            A[x][y] = new_pop
                        unions.append(union)
        if not unions:
            return print(days)

        days += 1

solution()
