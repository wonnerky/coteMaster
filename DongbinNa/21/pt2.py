# dfs 풀이
# recursion error 발생
# max recursion 깊이는 1000
# 이 코드는 max_n이 50으로 2500까지 탐색 경우 있음

import sys


def solution():
    def dfs(x, y, visited, union):
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(A[x][y] - A[nx][ny]) <= r:
                    union.append((nx, ny))
                    dfs(nx, ny, visited, union)

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
            for j in range(n):
                union = [(i, j)]
                if visited[i][j] == 0:
                    dfs(i, j, visited, union)
                    if len(union) > 1:
                        unions.append(union)
        if not unions:
            return print(days)
        for union in unions:
            total_pop = 0
            for x, y in union:
                total_pop += A[x][y]
            new_pop = total_pop // len(union)
            for x, y in union:
                A[x][y] = new_pop
        days += 1

solution()
